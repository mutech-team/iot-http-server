import uuid
from typing import Union
from django.db.models import QuerySet
from .models import Data, State, Device


def obtain_data(deviceid: uuid.UUID, data: str) -> Union[None, QuerySet]:
    try:
        return Data.objects.filter(device=obtain_device(deviceid), type=data)
    except Device.DoesNotExist:
        return None


def obtain_data_latest(deviceid: uuid.UUID, type: str) -> Union[None, Data]:
    try:
        data: Data = Data.objects.filter(device=obtain_device(
            deviceid), type=type).order_by('-id')[0]
        return data
    except Device.DoesNotExist:
        return None
    except IndexError:
        return None


def obtain_data_all(deviceid: uuid.UUID) -> Union[None, QuerySet]:
    try:
        return Data.objects.filter(device=obtain_device(deviceid))
    except Device.DoesNotExist:
        return None


def obtain_state(deviceid: uuid.UUID, state: str) -> Union[None, QuerySet]:
    try:
        return State.objects.filter(device=obtain_device(deviceid), type=state)
    except Device.DoesNotExist:
        return None


def obtain_state_all(deviceid: uuid.UUID) -> Union[None, QuerySet]:
    try:
        return State.objects.filter(device=obtain_device(deviceid))
    except Device.DoesNotExist:
        return None


def obtain_device(deviceid: uuid.UUID) -> Device:
    device: Device = Device.objects.get(mqtt_client_id=deviceid)
    return device
