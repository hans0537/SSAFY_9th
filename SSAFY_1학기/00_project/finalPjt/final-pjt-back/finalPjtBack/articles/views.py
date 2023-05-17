from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, CommentSerializer
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def articles_list_create(request):
    if request.method=='GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        print(request.data)
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
    
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_comment(request,article_pk):
#     if request.method=='POST':
#         article = Article.objects.get(pk=article_pk)
#         print(request.data)
#         serializer = CommentSerializer(article, data=request.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)

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