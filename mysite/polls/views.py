from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

    # 基本寫法
    # template = loader.get_template('polls/index2.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    
    # 快速寫法
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index2.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)