from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calculators/calculation.html')

def calculation(request):
    x = int(request.GET.get('x'))
    y = int(request.GET.get('y'))
    if y == 0:
        div = 0
    else:
        div = x / y

    content = {
        'x' : x,
        'y' : y,
        'mul' : x * y,
        'sub' : x - y,
        'div' : div,
    }

    return render(request, 'calculators/result.html', content)