from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import Feedback, Reservation

# Create your views here.

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'services/GiveFeedback.html'
    # fields = '__all__'
    fields = ['full_name','quality_of_food', 'portion_size', 'ease_of_ordering','overall_value', 'suggestions',]


class ThankyouView(TemplateView):
    template_name = 'services/ThankyouFeedback.html'



class ReservationView(CreateView):
    model = Reservation
    template_name = 'services/reservation.html'
    fields = ['full_name','booking_date','booking_time', 'total_person','contact_no','message']

    # fields = '__all__'


class TableConfirmView(TemplateView):
    template_name = 'services/TableConfirm.html'