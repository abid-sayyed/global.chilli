from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomerCreationForm(UserCreationForm):

    class meta:
        model = get_user_model()
        fields = ('username', 'email',)

class CustomUserchangeForm(UserChangeForm):

    class meta:
        model = get_user_model()
        fields = ('username', 'email',)