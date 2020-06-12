from django.contrib import admin
from .models import MQTTUser, Device, Data, State

admin.site.register(MQTTUser)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(State)
