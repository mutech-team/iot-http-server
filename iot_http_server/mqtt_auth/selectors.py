# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
import json
from typing import Dict
from mqtt_auth.models import User, Device


def auth_user(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    password: str = body_json["password"]
    try:
        User.objects.get(mqtt_username=username, mqtt_password=password)
        return True
    except Exception as e:
        return False


def auth_superuser(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    try:
        User.objects.get(mqtt_username=username, is_mqtt_superuser=True)
        return True
    except Exception as e:
        return False


def auth_topic(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    client_id: str = body_json["clientid"]
    topic: str = body_json["topic"]
    try:
        Device.objects.get(mqtt_client_id=client_id,
                           user=User.objects.get(mqtt_username=username))
        if topic.split("/")[2] != client_id:
            return False
        else:
            return True
    except Exception as e:
        return False
