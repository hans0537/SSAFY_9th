from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie,Genre
from rest_framework import status

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method=='GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request,movie_pk):
    if request.method=='GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movielike(request,movie_pk):
    if request.method=='POST':
        user = request.user
        movie = Movie.objects.get(pk=movie_pk)
        if movie.like_users.filter(pk=user.pk).exists():
          movie.like_users.remove(user)
        else:
          movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def review(request,movie_pk):
#     if request.method=='POST':
#         user = request.user
#         movie = Movie.objects.get(pk=movie_pk)
#         serializer = ReviewSerializer(data=request.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)