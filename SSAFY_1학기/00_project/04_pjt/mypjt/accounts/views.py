from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST, require_safe, require_http_methods


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index') 

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
    
    return redirect('movies:index') 

@require_safe
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('movies:index')

@require_POST
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
    return redirect('movies:index')