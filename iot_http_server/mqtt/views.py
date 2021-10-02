import uuid
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
import mqtt.selectors as selectors
import mqtt.services as services
import mqtt.serializers as serializers
import mqtt_auth.selectors as auth_selectors
import json


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
def obtain_data(request, deviceid, datatype):
    current_user_id = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    datatype = serializers.serialize(selectors.obtain_data(deviceid, datatype))
    return HttpResponse(datatype, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_data_latest(request, deviceid, datatype):
    current_user_id = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    datatype = serializers.serialize(selectors.obtain_data_latest(deviceid, datatype))
    return HttpResponse(datatype, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_data_all(request, deviceid):
    current_user_id = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data = serializers.serialize(selectors.obtain_data_all(deviceid))
    return HttpResponse(data, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_state(request, deviceid, statetype):
    current_user_id = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data = serializers.serialize(selectors.obtain_state(deviceid, statetype))
    return HttpResponse(data, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def obtain_state_all(request, deviceid):
    current_user_id = request.user.id
    if _DEBUG:
        if current_user_id is None:
            current_user_id = _DEBUG_USER_ID
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data = serializers.serialize(selectors.obtain_state_all(deviceid))
    return HttpResponse(data, content_type='application/json')


# @login_required(login_url='/login')
@conditional_decorator(login_required(login_url='/login'), not _DEBUG)
def save_state(request):
    try:
        body_json = json.loads(request.body)
        deviceid = body_json["deviceid"]
        current_user_id = request.user.id
        if _DEBUG:
            if current_user_id is None:
                current_user_id = _DEBUG_USER_ID
        if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
            return HttpResponse('Unauthorized to view this property', status=401)
        state = body_json["state"]
        value = body_json["value"]
        services.save_state(deviceid, state, value)
    except KeyError:
        return HttpResponse(400)
    return HttpResponse(200)
