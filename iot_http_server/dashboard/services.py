# Contains mypy-typed functions which write to the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from django.http import HttpRequest
from dashboard.forms import RegisterForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.db import IntegrityError


def register_user(request: HttpRequest) -> bool:
    form: RegisterForm = RegisterForm(request.POST)
    if form.is_valid():
        try:
            user = get_user_model().objects.create_user(username=form.cleaned_data['username'],
                                                        email=form.cleaned_data['email'],
                                                        password=form.cleaned_data['password'])
        except IntegrityError:
            return False
        login(request, user)
        return True
    return False
