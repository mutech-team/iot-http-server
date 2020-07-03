import uuid
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
import data.selectors as selectors
import data.services as services
import mqtt_auth.selectors as auth_selectors
import json
from typing import Dict


@login_required(login_url='/login')
def obtain_data(request: HttpRequest, deviceid: uuid, datatype: str) -> HttpResponse:
    current_user_id: int = request.user.id
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = serializers.serialize("json", selectors.obtain_data(deviceid, datatype), fields=('value', 'timestamp'))
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login')
def obtain_data_latest(request: HttpRequest, deviceid: uuid, datatype: str) -> HttpResponse:
    current_user_id: int = request.user.id
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    data: str = serializers.serialize("json", [selectors.obtain_data_latest(deviceid, datatype), ],
                                      fields=('value', 'timestamp'))
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login')
def save_state(request: HttpRequest):
    body_json: Dict[str, str] = json.loads(request.body)
    deviceid: str = body_json["deviceid"]
    current_user_id: int = request.user.id
    if not auth_selectors.userid_matches_deviceid(current_user_id, deviceid):
        return HttpResponse('Unauthorized to view this property', status=401)
    statetype: str = body_json["statetype"]
    value: str = body_json["value"]
    services.save_state(deviceid, statetype, value)
    return HttpResponse(200)
