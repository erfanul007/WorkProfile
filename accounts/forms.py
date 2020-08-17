from django.forms import ModelForm
from .models import UserInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UpdateUserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        exclude = ('username', 'date_created')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
