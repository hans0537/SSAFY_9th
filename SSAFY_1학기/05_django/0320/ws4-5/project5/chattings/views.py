from django.shortcuts import render, redirect
from .models import Chat

# Create your views here.
def index(request):
    chats = Chat.objects.all()
    context = {'chats' : chats}
    return render(request, 'chattings/index.html', context)

def new(request):
    return render(request, 'chattings/new.html')

def create(request):
    user = request.POST.get('user')
    content = request.POST.get('content')

    chat = Chat(user=user, content=content)
    chat.save()

    return redirect('chattings:index')

def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {'chat':chat}
    return render(request, 'chattings/detail.html',context)

def edit(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {'chat':chat}
    return render(request, 'chattings/edit.html',context)

def update(request, pk):
    chat = Chat.objects.get(pk=pk)
    
    user = request.POST.get('user')
    content = request.POST.get('content')

    chat.user = user
    chat.content = content
    chat.save()

    return redirect('chattings:detail', chat.pk)
