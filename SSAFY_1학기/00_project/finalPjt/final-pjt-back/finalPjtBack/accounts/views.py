from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, FriendListSerializer
from .models import User

# Create your views here.
@api_view(['GET'])
def findUsername(request):
    print(request.query_params)
    if request.method == "GET":
        user = User.objects.filter(email=request.query_params.get('email'))
        if user:
            serializer = UserSerializer(user[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT'])
def findPw(request):
    user = User.objects.filter(Q(email=request.query_params.get('email')) & Q(username = request.query_params.get('username')))
    if request.method == "GET":
        if user:
            serializer = UserSerializer(user[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        user[0].set_password(request.data.get('password1'))
        user[0].save()
        return Response({'message': '비밀번호가 성공적으로 변경되었습니다.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    if request.method == "GET":
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'username' : ''}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def userdelete(request):
    request.user.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request):
    if request.method == "PUT":
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def profile(request,user_pk):
    if request.method=='GET':
        user = get_object_or_404(get_user_model(),pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request,user_pk):
    if request.method=='POST':
        user = get_object_or_404(get_user_model(),pk=user_pk)
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def friends(request,user_pk):
    user = get_object_or_404(get_user_model(),pk=user_pk)
    if request.method=='GET':
        serializer = FriendListSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def setscore(request):
    user = request.user
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChoRank(request):
    # cho_points를 기준으로 내림차순 정렬 후 상위 10개만 가져옴
    choRank = User.objects.all().order_by('-cho_points')[:10]

    if request.method == 'GET':
        serializer = UserSerializer(choRank, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOverviewRank(request):
    # cho_points를 기준으로 내림차순 정렬 후 상위 10개만 가져옴
    overRank = User.objects.all().order_by('-overview_points')[:10]

    if request.method == 'GET':
        serializer = UserSerializer(overRank, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)