from django.contrib import admin
from .models import State, Data, MQTTUser, Device


admin.site.register(MQTTUser)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(State)
