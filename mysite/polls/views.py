from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , get_object_or_404
from django.template import loader
from .models import Question , Choice
from django.core.paginator import Paginator

# Create your views here.
# CBV = class base view

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")

    paginator = Paginator(latest_question_list, 3) # Each page contains 3 items
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    num_pages = [x for x in range(1,num_pages+1)]

    #data = {"latest_question_list":latest_question_list , "page_description":"Hello and welcome to this polls app"}
    return render(request,"polls/index.html",{'page': page,'page_count':num_pages})




def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    data = {"question" : question,"page_description":question.question_text,"content_date":question.pub_date}
    return render(request , "polls/detail.html",context=data)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    total_votes = 0

    for choice in question.choice_set.all():

        total_votes += choice.votes

     
    
    return render(request, "polls/results.html", {"question": question , 'total' : total_votes})


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError , Choice.DoesNotExist):
        data = {
                "question": question,
                "error_message": "You didn't select a choice.",
            }
        return render(request, "polls/detail.html",data)

    else:
        selected_choice.votes += 1
        selected_choice.save()

        data = {
                "question": question,
                "success_message": f"You voted on * {selected_choice.choice_text} * successfuly.",
            }
        return render(request, "polls/detail.html" , data)







def register(request):
    
    return render(request , "polls/register.html",context={})


