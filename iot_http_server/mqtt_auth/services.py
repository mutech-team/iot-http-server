# Contains mypy-typed functions which write to the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from mqtt.models import Device, MQTTUser
from django.contrib.auth import get_user_model


def _setup_test_user() -> None:
    user = get_user_model()(username="test_normal_user")
    user.save()
    mqtt_user = MQTTUser(user=user,
                         mqtt_username="49992d21-6cd2-4441-a94f-48df57215957",
                         mqtt_password="49992d21-6cd2-4441-a94f-48df57215957")
    mqtt_user.save()
    device = Device(user=user, name="test_device",
                    mqtt_client_id="d5e0531c-3dfb-4574-a1e8-7c83e783f7ec")
    device.save()


def _setup_test_superuser() -> None:
    superuser = get_user_model()(username="test_superuser")
    superuser.save()

    mqtt_superuser = MQTTUser(user=superuser,
                              mqtt_username="81f98bac-9048-491c-84a3-31dc5c488f2f",
                              mqtt_password="81f98bac-9048-491c-84a3-31dc5c488f2f",
                              is_mqtt_superuser=True)
    mqtt_superuser.save()


def setup_test_data() -> None:
    _setup_test_user()
    _setup_test_superuser()


def teardown_test_data() -> None:
    get_user_model().objects.filter(username="test_normal_user").delete()
    get_user_model().objects.filter(username="test_superuser").delete()
