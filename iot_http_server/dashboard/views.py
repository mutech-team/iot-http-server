from django.shortcuts import render
from dashboard.forms import LoginForm
from django.forms import Form
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from dashboard.selectors import authenticate_user


@login_required(login_url='/login')
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard/dashboard.html')


def login_view(request: HttpRequest) -> HttpResponse:
    form: Form
    if request.method == 'POST':
        if authenticate_user(request):
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'dashboard/login.html', {'form': form})


@login_required(login_url='/login')
def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    return HttpResponseRedirect('/')
