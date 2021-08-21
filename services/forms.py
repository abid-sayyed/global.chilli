from django import forms
# from django.forms import fields

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ['Customer']
