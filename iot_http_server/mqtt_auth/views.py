from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from mqtt_auth.selectors import auth_user, auth_superuser, auth_topic


def user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if auth_user(request.body):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def superuser(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if auth_superuser(request.body):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def topic(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if auth_topic(request.body):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)
