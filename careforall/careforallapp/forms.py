from django import forms
from django.contrib.auth.models import User
from careforallapp.models import UserProfileInfo

#LANGUAGE_CODE
class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
