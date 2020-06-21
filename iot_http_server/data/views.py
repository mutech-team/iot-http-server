import uuid
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
import data.selectors as selectors
import mqtt_auth.selectors as auth_selectors


@login_required(login_url='/login')
def obtain_data(request: HttpRequest, deviceid: uuid, datatype: str) -> JsonResponse:
    current_user_id: int = request.user.id
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = serializers.serialize("json", selectors.obtain_data(deviceid, datatype), fields=('value', 'timestamp'))
    # The Django REST framework then takes care of producing JSON for you
    # https://stackoverflow.com/questions/28249491/why-does-json-returned-from-the-django-rest-framework-have-forward-slashes-in-th
    return HttpResponse(data)


def obtain_data_latest(request: HttpRequest, deviceid: uuid, datatype: str) -> JsonResponse:
    current_user_id: int = request.user.id
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = serializers.serialize("json", [selectors.obtain_data_latest(deviceid, datatype), ],
                                      fields=('value', 'timestamp'))
    return HttpResponse(data)
