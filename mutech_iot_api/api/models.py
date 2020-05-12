from django.contrib.postgres.fields import JSONField
from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        db_table = 'Users'
        verbose_name_plural = 'Users'


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    state = JSONField()

    class Meta:
        db_table = 'Devices'
        verbose_name_plural = 'Devices'


class Data(models.Model):
    device = models.ForeignKey("Device", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=50)
    value = models.FloatField()

    class Meta:
        db_table = 'Data'
        verbose_name_plural = 'Data'
