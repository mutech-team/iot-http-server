import uuid
from .models import Data, State
from data import selectors
import modules.mqtt_publisher as mqtt_publisher


def save_state(deviceid: uuid.UUID, state: str, value: str) -> None:
    mqtt_publisher.publish(str(deviceid), state, value)
    device = selectors.obtain_device(deviceid)
    obj: State
    created: bool
    obj, created = State.objects.update_or_create(device=device, type=state)
    obj.value = value
    obj.serialized = obj.serialize_to_json()
    obj.save()
