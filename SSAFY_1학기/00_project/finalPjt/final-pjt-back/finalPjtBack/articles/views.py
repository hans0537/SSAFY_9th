from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, CommentCreateSerializer
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
    
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def comment_create_all(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user
    if request.method=='GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def comment_comment_create_all(request,article_pk,comment_pk):
    article = Article.objects.get(pk=article_pk)
    parent_comment = Comment.objects.get(pk=comment_pk)
    user = request.user

    if request.method=='GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)