from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Poll


def index(request):
    latest_polls = Poll.objects.all()
    context = {'latest_polls': latest_polls}
    return render(request, 'polls/index.html', context)


def detail_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/detail.html', context)


def vote_poll(request, poll_id, q_id, a_id):
    poll = get_object_or_404(Poll, id=poll_id)
    question = get_object_or_404(poll.questions.all(), id=q_id)
    answer = get_object_or_404(question.answers.all(), id=a_id)
    answer.votes = answer.votes + 1
    answer.save()
    return HttpResponseRedirect(reverse('poll_detail', kwargs={'poll_id': poll_id}))