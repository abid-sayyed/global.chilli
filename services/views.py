from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import Feedback, Reservation

# Create your views here.
class FeedbackView(LoginRequiredMixin,CreateView):
    model = Feedback
    template_name = 'services/GiveFeedback.html'
    login_url = 'account_login' # new
    fields = ['full_name','quality_of_food', 'portion_size', 'ease_of_ordering','overall_value', 'suggestions',]

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.customer = self.request.user
        # app_model.user = User.objects.get(user=self.request.user) # Or explicit model 
        app_model.save()
        return super().form_valid(form)






class ThankyouView(LoginRequiredMixin,TemplateView):
    template_name = 'services/ThankyouFeedback.html'
    login_url = 'account_login' # new


class ReservationView(LoginRequiredMixin,CreateView):
    model = Reservation
    template_name = 'services/reservation.html'
    fields = ['full_name','booking_date','booking_time', 'total_person','contact_no','message']
    login_url = 'account_login' # new
    # fields = '__all__'

class TableConfirmView(LoginRequiredMixin,TemplateView):
    template_name = 'services/TableConfirm.html'
    login_url = 'account_login' # new