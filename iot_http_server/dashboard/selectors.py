# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from django.http import QueryDict
from django.contrib.auth import authenticate, login
from dashboard.forms import LoginForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


def authenticate_user(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            username = get_user_model().objects.get(email=email).username
        except ObjectDoesNotExist:
            return False
        user = authenticate(username=username,
                            password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return True
    return False
