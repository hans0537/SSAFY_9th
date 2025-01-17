from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    Article.objects.get(pk = pk).delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk = pk)
    context = {'article' : article}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk = pk)
    
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content

    article.save()
    return redirect('articles:detail', pk)