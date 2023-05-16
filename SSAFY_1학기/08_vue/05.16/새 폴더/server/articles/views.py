from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleListSerializer
from .models import Articles

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def articles_list_create(request):
    if request.method == 'GET':
        articles = get_list_or_404(Articles)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        print('여기2', request.user)
        if serializer.is_valid(raise_exception=True):
            print('여기3', request.user)
            serializer.save(user=request.user)
            print('여기4', request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('asdf')
            print(serializer.errors)
