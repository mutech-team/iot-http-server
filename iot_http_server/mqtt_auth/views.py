from django.http import HttpResponse, HttpRequest
from mqtt_auth.selectors import auth_user, auth_superuser, auth_topic
from mqtt_auth.services import setup_test_data, teardown_test_data


def user(request):
    if request.method == 'POST':
        if auth_user(request.body):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def superuser(request):
    if request.method == 'POST':
        if auth_superuser(request.body):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def topic(request):
    if request.method == 'POST':
        if auth_topic(request.body):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def test_setup(request):
    if request.method == 'GET':
        setup_test_data()
        return HttpResponse(status=200)


def test_teardown(request):
    if request.method == 'GET':
        teardown_test_data()
        return HttpResponse(status=200)
