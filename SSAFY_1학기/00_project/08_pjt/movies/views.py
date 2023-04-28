from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, Genre
from django.contrib.auth import get_user_model

from django.http import JsonResponse

# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context = {
        'movie': movie,
    }

    return render(request, 'movies/detail.html', context)

@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            is_liked = False
        else:
            movie.like_users.add(user)
            is_liked = True

        context = {
            'is_liked': is_liked,
            'like_cnt': movie.like_users.count()
        }
        return JsonResponse(context)
    
    return redirect('accounts:login')

@require_safe
def recommended(request):
    user = request.user
    
    # 장르가 가장 많이 언급된 순서대로 저장할 딕셔너리
    genre = {}

    # 1번째 내가 좋아요 한 영화들의 장르들을 가져온다.
    for obj in user.like_movies.all():
        for g in obj.genres.all():
            if g.name in genre:
                genre[g.name] += 1
            else:
                genre[g.name] = 1

    # 2번째 내가 쓴 리뷰의 영화 제목들의 장르들을 가져온다.
    myMovieList = []
    for obj in user.review_set.all():
        myMovieList.append(obj.movie_title)

    for movie in myMovieList:
        # 영화 제목을 잘못 적었을 수 도 있으니 filter를 사용
        movie_obj = Movie.objects.filter(title=movie)

        for m in movie_obj:
            for g in m.genres.all():
                if g.name in genre:
                    genre[g.name] += 1
                else:
                    genre[g.name] = 1

    sorted_genres = sorted(genre, key=genre.get, reverse=True)
    top3 = []
    if len(sorted_genres) < 3:
        top3 = sorted_genres
    else:
        top3 = sorted_genres[:3]
    
    res_movies = []

    for genre in sorted_genres:
        gobj = Genre.objects.get(name=genre)
        for movie in gobj.movie_set.all():
            if movie not in res_movies:
                res_movies.append(movie)

    
    # 만약 회원이 아무 활동을 안해서 결과 영화배열에 아무것도 담겨 있지 않다면
    # 영화 평점 높은 순서대로 추천해준다.
    if not res_movies:
        res_movies = Movie.objects.order_by('-vote_average')


    context = {
        "top3" : top3,
        "res_movies" : res_movies
    }

    return render(request, 'movies/recommended.html', context)