from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, ReviewSerializers,ReviewcreateSerializers
from .models import Movie,Genre, Review
from rest_framework import status

# Create your views here.

@api_view(['GET'])
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
      
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def review_create_all(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    if request.method=='GET':
      revi = Review.objects.all()
      serializer = ReviewSerializers(revi, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ReviewcreateSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
          serializer.save(movie=movie, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)