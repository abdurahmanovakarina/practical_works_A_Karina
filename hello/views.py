from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import datetime

from django.urls import reverse
from django.views import View
from .models import Choice, Question


def query_time(request):
    query_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    context = {'query_time': query_time}
    return render(request, 'query_time.html', context)


def special(request):
    return render(request, 'special.html')


class IndexView(View):
    def get(self, request):
        latest_question_list = Question.objects.order_by('pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    total_votes = sum(c.votes for c in choices)
    percentages = [c.votes / total_votes * 100 if total_votes else 0 for c in choices]

    context = {
        'question': question,
        'choices': zip(choices, percentages)
    }
    return render(request, 'results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choices = request.POST.getlist('choice')
        if not selected_choices:
            raise KeyError
        if not question.multiple and len(selected_choices) > 1:
            raise ValueError
        for choice_id in selected_choices:
            choice = question.choice_set.get(pk=choice_id)
            choice.votes += 1
            choice.save()
    except KeyError:
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    except ValueError:
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You can only select one choice.",
        })
    else:
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
