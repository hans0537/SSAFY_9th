from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    # 여러개를 가져올때는 many=True 로 직렬화
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)