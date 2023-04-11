from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm 
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {'questions' : questions}
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save()
            return redirect('eithers:detail', q.pk)
    else:
        form = QuestionForm()
    
    context = {'form' : form}
    return render(request, 'eithers/create.html', context)

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    context = {
        'question' : question,
    }
    return render(request, 'eithers/detail.html', context)