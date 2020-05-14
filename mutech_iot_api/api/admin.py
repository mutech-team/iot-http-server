from django.contrib import admin
from api.models import User, Device, Data, State


admin.site.register(User)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(State)
