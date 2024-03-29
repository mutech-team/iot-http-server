import uuid
from .models import Data, State
import mqtt.selectors as selectors
import modules.mqtt_publisher as mqtt_publisher


def save_state(deviceid, state, value):
    mqtt_publisher.publish(str(deviceid), state, value)
    device = selectors.obtain_device(deviceid)  # type: ignore
    obj, created = State.objects.update_or_create(device=device, type=state)
    obj.value = value
    obj.serialized = obj.serialize_to_json()
    obj.save()
