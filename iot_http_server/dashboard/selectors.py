# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from django.http import QueryDict
from django.contrib.auth import authenticate, login
from dashboard.forms import LoginForm
from django.http import HttpRequest
from django.contrib.auth.models import User


def authenticate_user(request: HttpRequest) -> bool:
    form: LoginForm = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return True
    return False
