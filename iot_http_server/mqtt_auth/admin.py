from django.contrib import admin
from .models import MQTTUser, Device

admin.site.register(MQTTUser)
admin.site.register(Device)
