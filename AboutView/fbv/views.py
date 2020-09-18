from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse

# Create your views here.

# def index(request):
#     index_val = Question.objects
#     return render(request, 'fbv/index.html')

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'fbv/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question':question
    }
    return render(request, 'fbv/detail.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        return render(request, 'fbv/detail.html',{'question':question, 'error_msg':"you didn't select a choice."})
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('fbv:results', args(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'fbv/results.html', {'question':question})