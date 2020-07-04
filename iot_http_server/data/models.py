from django.db import models
from mqtt_auth.models import Device
from typing import Dict
import json


class Data(models.Model):
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
            self.serialized = models.TextField(json.dumps(data))
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
