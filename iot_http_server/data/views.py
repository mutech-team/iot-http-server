import uuid
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
import data.selectors as selectors
import data.services as services
import data.serializers as s
import mqtt_auth.selectors as auth_selectors
import json
from typing import Dict

_DEBUG = True
_DEBUG_USER_ID = 2


def conditional_decorator(dec, condition):
    def decorator(func):
        if not condition:
            return func
        return dec(func)

    return decorator


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_data(request: HttpRequest, deviceid: uuid, datatype: str) -> HttpResponse:
    current_user_id: int = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = s.serialize_data_queryset(selectors.obtain_data(deviceid, datatype))
    return HttpResponse(data, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_data_latest(request: HttpRequest, deviceid: uuid, datatype: str) -> HttpResponse:
    current_user_id: int = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = s.serialize_data_single(selectors.obtain_data_latest(deviceid, datatype))
    return HttpResponse(data, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_data_all(request: HttpRequest, deviceid: uuid) -> HttpResponse:
    current_user_id: int = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = s.serialize_data_queryset(selectors.obtain_data_all(deviceid))
    return HttpResponse(data, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def save_state(request: HttpRequest):
    body_json: Dict[str, str] = json.loads(request.body)
    deviceid: str = body_json["deviceid"]
    current_user_id: int = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    statetype: str = body_json["statetype"]
    value: str = body_json["value"]
    services.save_state(deviceid, statetype, value)
    return HttpResponse(200)
