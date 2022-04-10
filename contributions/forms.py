from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class IncomeForm(ModelForm):
    class Meta:
        model =  Source
        fields = "__all__"


class ExpencesForm(ModelForm):
    class Meta:
        model = Expenditure
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



