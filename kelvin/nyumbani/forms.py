from django.forms import ModelForm
from .models import *


class IncomeForm(ModelForm):
    class Meta:
        model =  Source
        fields = "__all__"


class ExpencesForm(ModelForm):
    class Meta:
        model = Expenditure
        fields = '__all__'

