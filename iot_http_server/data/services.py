import uuid
from .models import Data, State
from data import selectors


def save_state(deviceid: uuid, statetype: str, value: str) -> None:
    device = selectors.obtain_device(deviceid)
    obj, created = State.objects.update_or_create(device=device, type=statetype)
    obj.type = statetype
    obj.value = value
    obj.save()
