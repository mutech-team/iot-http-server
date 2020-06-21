from django.db import models
from mqtt_auth.models import  Device

# Create your models here.

class Data(models.Model):
    device: models.ForeignKey = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    type: models.CharField = models.CharField(max_length=50)
    value: models.TextField = models.TextField()

    def __str__(self):
        return self.type + " => " + self.value + " @ " + str(self.device.mqtt_client_id)

    class Meta:
        db_table = 'Data'
        verbose_name_plural = 'Data'


class State(models.Model):
    device: models.ForeignKey = models.ForeignKey(Device, on_delete=models.CASCADE)
    type: models.CharField = models.CharField(max_length=50)
    value: models.TextField = models.TextField()

    class Meta:
        db_table = 'States'
        verbose_name_plural = 'States'
