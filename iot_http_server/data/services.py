import uuid
from .models import Data, State
from data import selectors
import modules.mqtt_publisher as mqtt_publisher


def save_state(deviceid: uuid, state: str, value: str) -> None:
    mqtt_publisher.publish(deviceid, state, value)
    device = selectors.obtain_device(deviceid)
    obj, created = State.objects.update_or_create(device=device, type=state)
    obj.type = state
    obj.value = value
    obj.serialized = obj.serialize_to_json()
    obj.save()
