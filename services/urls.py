from django .urls import path
from .views import FeedbackView, ThankyouView, ReservationView, TableConfirmView

urlpatterns = [
    
    path('feedback/',FeedbackView.as_view(), name= 'feedback'),
    path('Thankyou/',ThankyouView.as_view(), name= 'ThankyouFeedback'),

    path('reservation/',ReservationView.as_view(), name= 'reservation'),

    path('confirmation/',TableConfirmView.as_view(), name= 'TableConfirm'),
    
]
