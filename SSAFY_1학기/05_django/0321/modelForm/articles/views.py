from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
    else:
        form = ArticleForm()
        
    context = {'form' : form}
    return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 업데이트시 instance=내가 가져온 모델 인자를 추가하면 바뀐 값만 수정하여 폼 업뎃이 된다
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
        
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
    else:
        # 기존의 값들을 가져와 form에 채워 넣는다
        form = ArticleForm(instance=article)

    context = {'form': form, 'article' : article}
    return render(request, 'articles/update.html', context)
