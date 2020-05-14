from django.db import models
import uuid


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    mqtt_username = models.UUIDField(default=uuid.uuid4)
    mqtt_password = models.UUIDField(default=uuid.uuid4)

    class Meta:
        db_table = 'Users'
        verbose_name_plural = 'Users'


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mqtt_client_id = models.UUIDField(default=uuid.uuid4)

    class Meta:
        db_table = 'Devices'
        verbose_name_plural = 'Devices'


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.ForeignKey("Device", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    value = models.FloatField()

    class Meta:
        db_table = 'Data'
        verbose_name_plural = 'Data'


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.ForeignKey("Device", on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    value = models.FloatField()

    class Meta:
        db_table = 'States'
        verbose_name_plural = 'States'
