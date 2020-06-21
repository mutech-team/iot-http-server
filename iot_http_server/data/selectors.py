from uuid import UUID
from django.db.models import QuerySet
from mqtt_auth.models import Device
from .models import Data, State


def obtain_data(deviceid: UUID, datatype: str) -> QuerySet:
    try:
        return Data.objects.filter(device=Device.objects.get(mqtt_client_id=deviceid), type=datatype)
    except Device.DoesNotExist:
        return []


def obtain_data_latest(deviceid: UUID, datatype: str) -> Data:
    try:
        return Data.objects.filter(device=Device.objects.get(mqtt_client_id=deviceid), type=datatype).order_by('-id')[0]
    except Device.DoesNotExist:
        return []


def obtain_device(deviceid: UUID) -> Device:
    return Device.objects.get(mqtt_client_id=deviceid)

