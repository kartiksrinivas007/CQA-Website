from django import forms
from django.contrib.auth.forms import UserCreationForm

from cqa.models import CustomUser

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    display_name = forms.CharField(max_length=255)
    about_me = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'about_me', 'password1', 'password2')
        