from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    event_name = forms.CharField(max_length=100, label='Event Name')
    event_place = forms.CharField(max_length=100, label='Event Place')
    event_time = forms.DateTimeField(label='Event Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    description = forms.CharField(widget=forms.Textarea, label='Description')