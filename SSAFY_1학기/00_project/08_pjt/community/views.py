from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

from django.http import JsonResponse
import json

@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)

    json_data = json.loads(request.body)
    comment_form = CommentForm(json_data)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()

    context = {
        'user': request.user.username,
        'review_pk': review.pk,
        'comment_pk': comment.pk,
        'comment_counts': review.comment_set.count()
    }
    return JsonResponse(context)

@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False
        else:
            review.like_users.add(user)
            is_liked = True

        context = {
            'is_liked': is_liked,
            'like_cnt': review.like_users.count()
        }
        return JsonResponse(context)
    
    return redirect('accounts:login')


def co_comments_create(request, review_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    review = Review.objects.get(pk=review_pk)
    parent_comment = Comment.objects.get(pk=comment_pk)

    json_data = json.loads(request.body)
    comment_form = CommentForm(json_data)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.parent_comment = parent_comment
        comment.save()

    context = {
        'user': request.user.username,
        'review_pk': review.pk,
        'parent_comment_pk': parent_comment.pk,
        'comment_pk': comment.pk,
        'comment_counts': review.comment_set.count()
    }

    return JsonResponse(context)
