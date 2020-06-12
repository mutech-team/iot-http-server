# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
import json
from typing import Dict
from mqtt_auth.models import Device, MQTTUser
from django.contrib.auth.models import User


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


def auth_topic(body: str) -> bool:
    body_json: Dict[str, str] = json.loads(body)
    username: str = body_json["username"]
    client_id: str = body_json["clientid"]
    topic: str = body_json["topic"]
    acc: int = int(body_json["acc"])
    try:
        if acc == 2:
            """
            Client is wanting to publish to the mqtt server.
            The topic format must be /ingest/clientid/channel.
            In addition to that, the clientid must match the username.
            If it is not, return false.
            """
            if topic.split("/")[1] != "ingest":
                return False
            if topic.split("/")[2] != client_id:
                return False
            Device.objects.get(mqtt_client_id=client_id, user=MQTTUser.objects.get(mqtt_username=username).user)
        elif acc == 4:
            """
            Client is wanting to subscribe to a topic and receive
            the data from the mqtt server.
            The topic format must be /clientid/channel.
            In addition to that, the clientid must match the username.
            If it is not, return false. 
            """
            if topic.split("/")[1] != client_id:
                return False
            Device.objects.get(mqtt_client_id=client_id, user=MQTTUser.objects.get(mqtt_username=username).user)
        else:
            return False
        return True
    except Exception as e:
        return False
