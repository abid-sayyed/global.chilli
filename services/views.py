from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import Feedback

# Create your views here.

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'services/GiveFeedback.html'
    # fields = '__all__'
    fields = ['quality_of_food', 'portion_size', 'ease_of_ordering','overall_value', 'suggestions',]


class ThankyouView(TemplateView):
    template_name = 'services/ThankyouFeedback.html'