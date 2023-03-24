from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm

# Create your views here.
@require_safe
def index(request):
    # 모달로 회원가입, 로그인을 하기 위한 폼 전달
    loginForm = AuthenticationForm()
    signupForm = CustomUserCreationForm()

    # 로그인 되어 있을때 create하기 위함
    msg = ''
    if not request.user.is_authenticated:
        msg = "로그인후에 이용하세요"

    movies = Movie.objects.order_by('pk')
    context = {'movies' : movies, 'loginForm' : loginForm, 'signupForm' : signupForm, 'msg' : msg}
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    
    context = {'form' : form}
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    # 모달로 회원가입, 로그인을 하기 위한 폼 전달
    loginForm = AuthenticationForm()
    signupForm = CustomUserCreationForm()
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie' : movie, 'loginForm' : loginForm, 'signupForm' : signupForm}
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            print('>>', form)
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    
    context = {'form' : form, 'movie' : movie}
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
    return redirect('movies:index')

