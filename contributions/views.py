from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

from django.db.models import Sum


def registrerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account for "{}" was created successfully'.format(username))
                return redirect('contributions:login')
        context = {'registerform': form}
        return render(request, 'Contributions/accounts/register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('contributions:nyumbani')
        else:
            messages.info(request, "Usename OR Password is incorrect !!!")

    context = {}
    return render(request, 'Contributions/accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'Contributions/accounts/logout.html')


@login_required(login_url='contributions:login')
def home(request):
    matumizi = Expenditure.objects.all()
    fundSource = Source.objects.all()
    totalexp = matumizi.aggregate(amount=Sum('amount'))

    totalinc = fundSource.aggregate(amount=Sum('amount'))

    context = {
        "matumizi": matumizi,
        "source": fundSource,
        "totalexp": totalexp,
        "totalinc": totalinc,

    }
    return render(request, 'Contributions/ndani.html', context)


@login_required(login_url='contributions:login')
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
        'matumizi': matumizi[::-1],
        'expform': expform,
        'totalexp': totalexp,
    }
    return render(request, 'Contributions/expenditure.html', context)


@login_required(login_url='contributions:login')
def source(request):
    fundSource = Source.objects.all()
    totalinc = fundSource.aggregate(amount=Sum('amount'))
    sourcform = IncomeForm()
    if request.method == 'POST':
        sourcform = IncomeForm(request.POST)
        if sourcform.is_valid():
            sourcform.save()
            return redirect('contributions:nyumbani')
    context = {
        'fundSource': fundSource[::-1],
        'srcform': sourcform,
        'totalinc': totalinc,
    }
    return render(request, 'Contributions/income.html', context)


