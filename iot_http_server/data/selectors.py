import uuid
from typing import Union

from django.db.models import QuerySet
from mqtt_auth.models import Device
from .models import Data, State


def obtain_data(deviceid: uuid, data: str) -> Union[None, QuerySet]:
    try:
        return Data.objects.filter(device=obtain_device(deviceid), type=data)
    except Device.DoesNotExist:
        return None


def obtain_data_latest(deviceid: uuid, data: str) -> Union[None, QuerySet]:
    try:
        return Data.objects.filter(device=obtain_device(deviceid), type=data).order_by('-id')[0]
    except Device.DoesNotExist:
        return None
    except IndexError:
        return None


def obtain_data_all(deviceid: uuid) -> Union[None, QuerySet]:
    try:
        return Data.objects.filter(device=obtain_device(deviceid))
    except Device.DoesNotExist:
        return None


def obtain_state(deviceid: uuid, state: str) -> Union[None, QuerySet]:
    try:
        return State.objects.filter(device=obtain_device(deviceid), type=state)
    except Device.DoesNotExist:
        return None


def obtain_state_all(deviceid: uuid) -> Union[None, QuerySet]:
    try:
        return State.objects.filter(device=obtain_device(deviceid))
    except Device.DoesNotExist:
        return None


def obtain_device(deviceid: uuid) -> Device:
    return Device.objects.get(mqtt_client_id=deviceid)
