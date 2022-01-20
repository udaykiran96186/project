from django import forms
from django.forms import fields
from django.forms.widgets import PasswordInput
from app1.models import CreateAccount

class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = CreateAccount
        fields = "__all__"


# class LoginForm(forms.Form):
#     userName = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())

from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')
