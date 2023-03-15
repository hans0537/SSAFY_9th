from django.shortcuts import render
import random, datetime

# Create your views here.
age = range(25, 31)
grade = ['a', 'b', 'c', 's']
def certification1(request):
    content = {
        'name' : '김민국',
        'age' : age,
        'grade' : grade,
        'today' : datetime.datetime.now
    }
    return render(request, 'certifications/certification1.html', content)

def certification2(request):
    content = {
        'name' : '임준환',
        'age' : age,
        'grade' : grade,
    }
    return render(request, 'certifications/certification2.html', content)


def certification3(request):
    content = {
        'name' : '이금규',
        'age' : age,
        'grade' : grade,
    }
    return render(request, 'certifications/certification3.html', content)

