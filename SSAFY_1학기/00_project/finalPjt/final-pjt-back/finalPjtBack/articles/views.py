from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, CommentCreateSerializer, CoCommentCreateSerializer
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def articles_list_create(request):
    if request.method=='GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request,article_pk):
    if request.method=='GET':
        article = Article.objects.get(pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def comment_create_all(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user
    if request.method=='GET':
        parent_comments = Comment.objects.filter(article=article, parent_comment=None).order_by('-created_at')
        parent_comments_serializer = CommentSerializer(parent_comments, many=True)

        parent_comments_ids = parent_comments.values_list('id', flat=True)
        child_comments = Comment.objects.filter(article=article, parent_comment__in=parent_comments_ids).order_by('-created_at')
        child_comments_serializer = CommentSerializer(child_comments, many=True)

        serialized_data = parent_comments_serializer.data
        for parent_comment in serialized_data:
            parent_comment_id = parent_comment['id']
            parent_comment['child_comments'] = [comment for comment in child_comments_serializer.data if comment['parent_comment'] == parent_comment_id]

        return Response(serialized_data, status=status.HTTP_200_OK)
    else:
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request,article_pk):
    if request.method=='POST':
        user = request.user
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
        else:
            article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_comment_create_all(request,article_pk,comment_pk):
    article = Article.objects.get(pk=article_pk)
    parent_comment = Comment.objects.get(pk=comment_pk)
    user = request.user

    if request.method == "POST":
        serializer = CoCommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, parent_comment=parent_comment, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# 조회수 증가
@api_view(['PUT'])
def hit(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'PUT':
        article.hit = article.hit + 1
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
