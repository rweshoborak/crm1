from django.shortcuts import render, redirect
from .models import *
from .forms import  *
from django.db.models import Sum


def home(request):
    matumizi = Expenditure.objects.all()
    fundSource = Source.objects.all()
    totalexp = matumizi.aggregate(amount=Sum('amount'))

    totalinc = fundSource.aggregate(amount=Sum('amount'))



    context = {
        "matumizi": matumizi,
        "source": fundSource,
        "expences": totalexp,
        "totalinc": totalinc,


    }
    return render(request, 'Contributions/ndani.html', context)


def expenses(request):
    matumizi = Expenditure.objects.all()
    totalexp = matumizi.aggregate(amount=Sum('amount'))
    expform = ExpencesForm()
    if request.method == 'POST':
        expform = ExpencesForm(request.POST)
        if expform.is_valid():
            expform.save()
            return redirect('contributions:expenditure')

    context = {
       'matumizi': matumizi,
        'expform': expform,
        'totalexp': totalexp,
    }
    return render(request, 'Contributions/expenditure.html', context)


def source(request):
    fundSource = Source.objects.all()
    totalinc = fundSource.aggregate(amount=Sum('amount'))
    sourcform = IncomeForm()
    if request.method == 'POST':
        sourcform= IncomeForm(request.POST)
        if sourcform.is_valid():
            sourcform.save()
            return redirect('contributions:nyumbani')
    context = {
        'fundSource': fundSource,
        'srcform': sourcform,
        'totalinc': totalinc,
    }
    return render(request, 'Contributions/income.html', context)


