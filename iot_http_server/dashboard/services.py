# Contains mypy-typed functions which write to the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from django.http import HttpRequest
from dashboard.forms import RegisterForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.db import IntegrityError

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_forgot_password_email(recipient_email: str, recipient_name: str, reset_url: str) -> None:
    # TODO: Create a function which will reset the user password inside selector
    context = {}
    context["name"] = "Test User Made By IcE"
    context["action_url"] = "mutech.ivica.codes"
    html_message = render_to_string('email/reset_password_email.html', context)
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    to = 'to@example.com'
    send_mail("Reset your password", plain_message, email_from, [recipient_email], html_message=html_message)


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
