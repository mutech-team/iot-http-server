from django.shortcuts import render
from dashboard.forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from dashboard.selectors import authenticate_user
from dashboard.services import register_user


@login_required(login_url='/login')
def index(request):
    return render(request, 'dashboard/dashboard.html')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        if authenticate_user(request):
            return HttpResponseRedirect('/')
    return render(request, 'dashboard/accounts/login.html', {'form': form})


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        if register_user(request):
            return HttpResponseRedirect('/')
    return render(request, 'dashboard/accounts/register.html', {'form': form})


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
