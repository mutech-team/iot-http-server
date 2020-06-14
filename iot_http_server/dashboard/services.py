# Contains mypy-typed functions which write to the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from django.http import HttpRequest
from dashboard.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def register_user(request: HttpRequest) -> bool:
    form: RegisterForm = RegisterForm(request.POST)
    if form.is_valid():
        user: User = User.objects.create_user(username=form.cleaned_data['username'],
                                              email=form.cleaned_data['email'],
                                              password=form.cleaned_data['password'])
        login(request, user)
        return True
    return False
