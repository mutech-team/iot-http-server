from django.db import models
from django.contrib.auth import get_user_model
import uuid


class MQTTUser(models.Model):
    user: models.OneToOneField = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    mqtt_username: models.UUIDField = models.UUIDField(default=uuid.uuid4)
    mqtt_password: models.UUIDField = models.UUIDField(default=uuid.uuid4)
    is_mqtt_superuser: models.BooleanField = models.BooleanField(default=False)

    def __str__(self):
        return str(self.mqtt_username)

    class Meta:
        db_table = 'MQTTUsers'
        verbose_name_plural = 'MQTTUsers'


class Device(models.Model):
    user: models.ForeignKey = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=50)
    mqtt_client_id: models.UUIDField = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return str(self.mqtt_client_id)

    class Meta:
        db_table = 'Devices'
        verbose_name_plural = 'Devices'


