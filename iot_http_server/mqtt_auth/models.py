from django.db import models
from django.contrib.auth.models import User
import uuid


class MQTTUser(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)
    mqtt_username: models.UUIDField = models.UUIDField(default=uuid.uuid4)
    mqtt_password: models.UUIDField = models.UUIDField(default=uuid.uuid4)
    is_mqtt_superuser: models.BooleanField = models.BooleanField(default=False)

    class Meta:
        db_table = 'MQTTUsers'
        verbose_name_plural = 'MQTTUsers'


class Device(models.Model):
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=50)
    mqtt_client_id: models.UUIDField = models.UUIDField(default=uuid.uuid4)

    class Meta:
        db_table = 'Devices'
        verbose_name_plural = 'Devices'


class Data(models.Model):
    device: models.ForeignKey = models.ForeignKey("Device", on_delete=models.CASCADE)
    timestamp: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    type: models.CharField = models.CharField(max_length=50)
    value: models.TextField = models.TextField()

    class Meta:
        db_table = 'Data'
        verbose_name_plural = 'Data'


class State(models.Model):
    device: models.ForeignKey = models.ForeignKey("Device", on_delete=models.CASCADE)
    type: models.CharField = models.CharField(max_length=50)
    value: models.TextField = models.TextField()

    class Meta:
        db_table = 'States'
        verbose_name_plural = 'States'