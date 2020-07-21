import uuid
from django.db.models import QuerySet
from .models import Data, State, Device


def obtain_data(deviceid, datatype):
    try:
        return Data.objects.filter(device=obtain_device(deviceid), type=datatype)
    except Device.DoesNotExist:
        return None


def obtain_data_latest(deviceid, datatype):
    try:
        data = Data.objects.filter(device=obtain_device(
            deviceid), type=datatype).order_by('-id')[0]
        return data
    except Device.DoesNotExist:
        return None
    except IndexError:
        return None


def obtain_data_all(deviceid):
    try:
        return Data.objects.filter(device=obtain_device(deviceid))
    except Device.DoesNotExist:
        return None


def obtain_state(deviceid, statetype):
    try:
        return State.objects.filter(device=obtain_device(deviceid), type=statetype)
    except Device.DoesNotExist:
        return None


def obtain_state_all(deviceid):
    try:
        return State.objects.filter(device=obtain_device(deviceid))
    except Device.DoesNotExist:
        return None


def obtain_device(deviceid):
    device = Device.objects.get(mqtt_client_id=deviceid)
    return device
