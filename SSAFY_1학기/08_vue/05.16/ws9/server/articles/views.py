from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleListSerializer
from .models import Article

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def articles_list_create(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
