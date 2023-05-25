from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import MovieSerializer, ReviewSerializers,ReviewcreateSerializers, GenreSerializers
from .models import Movie,Genre, Review, NowMovie, UpMovie, PopularMovie
from rest_framework import status

# Create your views here.

# 전체 영화 조회
@api_view(['GET'])
def index(request):
    if request.method=='GET':
      movie = Movie.objects.all()
      serializer = MovieSerializer(movie,many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
# 장르 조회
@api_view(['GET'])
def genre(request):
    if request.method=='GET':
        genre = Genre.objects.all()
        serializer = GenreSerializers(genre,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 현재 상영작 조회
@api_view(['GET'])
def nowmovie(request):
    if request.method=='GET':
        movie = NowMovie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 상영 예정작 조회
@api_view(['GET'])
def upcommovie(request):
    if request.method=='GET':
        movie = UpMovie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
# 인기 영화 조회
@api_view(['GET'])
def popularmovie(request):
    if request.method=='GET':
        movie = PopularMovie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

      
@api_view(['GET'])
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
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def worldcuplike(request,movie_pk):
    if request.method=='POST':
        user = request.user
        movie = Movie.objects.get(pk=movie_pk)
        if movie.worldcup_users.filter(pk=user.pk).exists():
          pass
        else:
          movie.worldcup_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['POST','GET'])
# 작성만 인증하기 가져오는건 인증 X
@permission_classes([IsAuthenticatedOrReadOnly])
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
      
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_del(request, movie_pk, comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    revi = Review.objects.get(pk=comment_pk)
    user = request.user
    if request.method=='PUT':
        serializer = ReviewcreateSerializers(revi, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        revi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)