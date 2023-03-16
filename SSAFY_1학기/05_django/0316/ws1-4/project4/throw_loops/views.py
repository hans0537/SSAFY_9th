from django.shortcuts import render

# Create your views here.
def first(request):
    c = request.GET.get('throw')
    
    if c is None:
        c = 0
    
    content = {
        'c' : c
    }
    return render(request, 'throw_loops/first.html', content)

def second(request):
    c = request.GET.get('throw')

    content = {
        'c' : c
    }
    return render(request, 'throw_loops/second.html', content)


def third(request):
    lst = []
    lst.append(request.GET.get('throw1'))
    lst.append(request.GET.get('throw2'))
    
    content = {
        'lst':lst
    }
    print(lst)
    return render(request, 'throw_loops/third.html', content)