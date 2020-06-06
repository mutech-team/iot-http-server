# Contains mypy-typed functions which write to the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
from mqtt_auth.models import User, Device


def setup_test_data() -> None:
    test_normal_user = User(username="test_normal_user",
                            mqtt_username="49992d21-6cd2-4441-a94f-48df57215957",
                            mqtt_password="49992d21-6cd2-4441-a94f-48df57215957")
    test_normal_user.save()

    test_superuser = User(username="test_superuser",
                          mqtt_username="81f98bac-9048-491c-84a3-31dc5c488f2f",
                          mqtt_password="81f98bac-9048-491c-84a3-31dc5c488f2f",
                          is_mqtt_superuser=True)
    test_superuser.save()

    test_device = Device(user=test_normal_user, name="test_device",
                         mqtt_client_id="d5e0531c-3dfb-4574-a1e8-7c83e783f7ec")
    test_device.save()


def teardown_test_data() -> None:
    User.objects.filter(username="test_normal_user").delete()
    User.objects.filter(username="test_superuser").delete()
