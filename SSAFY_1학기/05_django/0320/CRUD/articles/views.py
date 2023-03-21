from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, id):
    article = Article.objects.get(pk=id)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 이방법은 바로 저장한다
        # Article.objects.create(title=title, content=content)

        # 그러나 이방법을 주로 사용
        # 저장하기 전에 검사를 해야 하기 때문
        article = Article(title=title, content=content)
        article.save()

    # forward 방식 : 요청, 응답 정보를 그대로 계속 가져감, 페이지만 바뀐다. => 계속 포워딩 가능, url 유지
    # 시스템에 변화가 생기지 않는 단순 조회 요청
    # return render(request, "articles/index.html")
    
    # redirect 방식 : 새로운 요청을 생성(기존 요청,응답 정보가 제거됨) => url 변경
    # 시스템에 변화가 생기는 새로운 요청
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')


def delete(request, id):
    Article.objects.get(pk=id).delete()
    return redirect('articles:index')

# def edit(request, id):
#     article = Article.objects.get(pk=id)
#     context = {
#         'article' : article,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        article = Article.objects.get(pk = id)
        title = request.POST.get('title')
        content = request.POST.get('content')

        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)
    else:
        article = Article.objects.get(pk=id)
        context = {
            'article' : article,
        }
        return render(request, 'articles/edit.html', context)