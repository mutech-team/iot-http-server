from django.db import models
from typing import Dict
import json
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


class Data(models.Model):
    device: models.ForeignKey = models.ForeignKey(Device, on_delete=models.CASCADE)
    device: models.ForeignKey = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    type: models.CharField = models.CharField(max_length=50)
    value: models.TextField = models.TextField()
    serialized: models.TextField = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.device.mqtt_client_id)

    def serialize_to_json(self) -> str:
        if self.serialized is None:
            data: Dict[str, str] = {"deviceid": str(self.device.mqtt_client_id), "timestamp": str(self.timestamp),
                                    "type": str(self.type), "value": str(self.value)}
            self.serialized = json.dumps(data)
            self.save()
            return str(self.serialized)
        else:
            return str(self.serialized)

    class Meta:
        db_table = 'Data'
        verbose_name_plural = 'Data'


class State(models.Model):
    device: models.ForeignKey = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    type: models.CharField = models.CharField(max_length=50)
    value: models.TextField = models.TextField()
    serialized: models.TextField = models.TextField(default=None, null=True)

    def serialize_to_json(self) -> str:
        data: Dict[str, str] = {"deviceid": str(self.device.mqtt_client_id), "timestamp": str(self.timestamp),
                                "type": str(self.type), "value": str(self.value)}
        return json.dumps(data)

    class Meta:
        db_table = 'States'
        verbose_name_plural = 'States'
