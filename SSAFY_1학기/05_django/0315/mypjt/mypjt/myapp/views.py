from django.shortcuts import render

# Create your views here.
def home(request):
    name = 'aiden'

    info = {
        'name' : 'aiden',
        'age'   : 19
    }
    return render(request, 'myapp/hello.html', {'info' : info})

def fruit(request):
    food = {
        'fruit' : ['apple', 'melon', 'banana',]
    }

    return render(request, 'myapp/fruits.html', food)

def template(request):
    return render(request, 'myapp/template.html')