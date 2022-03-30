from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    
    data = {
        "latest_question_list":latest_question_list,
    }
    
    return render(request, "polls/index.html",data)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    data = {
        "question":question
    }
    
    return render(request, 'polls/detail.html', data)


def results(request,question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero  {question_id}")


def vote(request,question_id):
    return HttpResponse(f"Estas votando a la pregunta numero  {question_id}")
    