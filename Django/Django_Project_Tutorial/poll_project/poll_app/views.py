from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'poll_app/index.html'
    context_object_name = 'latest_que_list'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be
        published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll_app/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll_app/results.html'

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, "poll_app/detail.html", {'question':question, 'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_app:results',args=(question.id,)))
    return HttpResponse("Vote for question %s" % question_id)


##############################################################################################################################################
# default DetailView name = <app name>/<model name>_detail.html           "poll_app/question_detail.html"
# default ListView name = <app name>/<model name>_list.html               "poll_app/question_list.html"
# DetailView context variable name = <model_name> with lowercase          "question"
# ListView context variable name = <model_name>_list                      "question_list"
# To override this variables default name we have used template_name, context_object_name parameters
###############################################################################################################################################

# def index(request):
#     latest_que_list = Question.objects.order_by('-pub_date')[:5]
#     return render(request, 'poll_app/index.html', { 'latest_que_list' : latest_que_list }   )
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id )
#     return render(request, "poll_app/detail.html", { 'question' : question })
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id )
#     return render(request, "poll_app/results.html", {"question" : question} )
