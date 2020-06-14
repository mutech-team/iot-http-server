# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
import json
from typing import Dict
from mqtt_auth.models import Device, MQTTUser
from django.contrib.auth.models import User

_PUBLISH_ACTION_ID: int = 2
_SUBSCRIBE_ACTION_ID: int = 4


def auth_user(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    password: str = body_json["password"]
    try:
        MQTTUser.objects.get(mqtt_username=username, mqtt_password=password)
        return True
    except Exception as e:
        return False


def auth_superuser(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    try:
        MQTTUser.objects.get(mqtt_username=username, is_mqtt_superuser=True)
        return True
    except Exception as e:
        return False


def _client_id_matches_username(client_id: str, username: str) -> bool:
    try:
        Device.objects.get(mqtt_client_id=client_id,
                           user=MQTTUser.objects.get(mqtt_username=username).user)
    except Exception as e:
        return False
    else:
        return True


def _topic_is_valid(topic: str, client_id: str, action_id: int) -> bool:
    if (action_id == _PUBLISH_ACTION_ID
            and topic.split("/")[1] == "ingest"
            and topic.split("/")[2] == client_id):
        return True
    elif (action_id == _SUBSCRIBE_ACTION_ID
          and topic.split("/")[1] == client_id):
        return True
    else:
        return False


def auth_topic(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    client_id: str = body_json["clientid"]
    topic: str = body_json["topic"]
    action_id: int = int(body_json["acc"])
    if (_client_id_matches_username(client_id, username)
            and _topic_is_valid(topic, client_id, action_id)):
        return True
    else:
        return False
