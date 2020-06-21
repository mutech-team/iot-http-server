from .models import Data, State
from .selectors import obtain_device


def save_state(deviceid: str, statetype: str, value: str) -> None:
    device = obtain_device(deviceid)
    obj, created = State.objects.update_or_create(device=device,type=statetype)
    obj.type = statetype
    obj.value = value
    obj.save()
