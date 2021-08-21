from django .urls import path
from .views import FeedbackView, ThankyouView

urlpatterns = [
    
    path('feedback',FeedbackView.as_view(), name= 'feedback'),
    path('Thankyou',ThankyouView.as_view(), name= 'ThankyouFeedback'),
    
]
