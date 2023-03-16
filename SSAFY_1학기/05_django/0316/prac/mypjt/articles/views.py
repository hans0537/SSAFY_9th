from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # request.GET의 반환값은 딕셔너리 형태

    print(request.GET.get('message'))
    print(request.GET.get('key'))

    context = {
        'message' : request.GET.get('message'),
        'key'     : request.GET["key"]
    }

    return render(request, 'articles/catch.html', context)