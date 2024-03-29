# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
import json
import uuid
import user_unique_email
from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from mqtt.models import Device, MQTTUser


_PUBLISH_ACTION_ID: int = 2
_SUBSCRIBE_ACTION_ID: int = 4


def auth_user(body):
    body_json = json.loads(body)
    username = body_json["username"]
    password = body_json["password"]
    try:
        MQTTUser.objects.get(mqtt_username=uuid.UUID(username), mqtt_password=uuid.UUID(password))
        return True
    except (MQTTUser.DoesNotExist, ValueError):
        return False


def auth_superuser(body):
    body_json: Dict[str, str] = json.loads(body)
    username = body_json["username"]
    try:
        MQTTUser.objects.get(mqtt_username=uuid.UUID(username), is_mqtt_superuser=True)
        return True
    except (MQTTUser.DoesNotExist, ValueError):
        return False


def userid_matches_deviceid(userid, deviceid):
    try:
        result = Device.objects.get(
            user=get_user_model().objects.get(id=userid), mqtt_client_id=deviceid)
        if result:
            return True
        return False
    except user_unique_email.models.User.DoesNotExist:
        return False
    except Device.DoesNotExist:
        return False


def _client_id_matches_username(client_id, username):
    try:
        Device.objects.get(mqtt_client_id=client_id,
                           user=MQTTUser.objects.get(mqtt_username=uuid.UUID(username)).user)
    except (user_unique_email.models.User.DoesNotExist, ValueError, Device.DoesNotExist):
        return False
    else:
        return True


def _topic_is_valid(topic, client_id, action_id):
    if (action_id == _PUBLISH_ACTION_ID
            and topic.split("/")[1] == "ingest"
            and topic.split("/")[2] == str(client_id)):
        return True
    elif (action_id == _SUBSCRIBE_ACTION_ID
          and topic.split("/")[1] == str(client_id)):
        return True
    else:
        return False


def auth_topic(body):
    body_json = json.loads(body)
    username = body_json["username"]
    client_id = uuid.UUID(body_json["clientid"])
    topic = body_json["topic"]
    action_id = int(body_json["acc"])
    if (_client_id_matches_username(client_id, username)
            and _topic_is_valid(topic, client_id, action_id)):
        return True
    else:
        return False
