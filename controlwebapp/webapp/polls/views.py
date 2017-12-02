# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import unittest
import logging
from .models import Choice, Question, TemperatureReading
# Create your views here.
import arrow
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import random
<<<<<<< HEAD
from decimal import Decimal

=======
>>>>>>> 62de621f44c02fa21d5e9ecc610984225d516ddb

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class AnalyticsIndexView(TemplateView):
    template_name = 'polls/chart.html'
    def get_context_data(self, **kwargs):
        context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
        context['30_day_registrations'] = self.thirty_day_registrations()
        return context

    def thirty_day_registrations(self):
        final_data = []
<<<<<<< HEAD
        all_temperature_readings = TemperatureReading.objects.all()
        for current_temperature_reading in all_temperature_readings:
            final_data.append(float(current_temperature_reading.tempvalue))
            print current_temperature_reading.tempvalue
        print final_data
=======
        date = arrow.now()
        for day in xrange(1, 30):
            date = date.replace(days=-1)
            count = random.randint(1,100)
            final_data.append(count)
>>>>>>> 62de621f44c02fa21d5e9ecc610984225d516ddb
        return final_data


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
