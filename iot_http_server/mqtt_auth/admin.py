from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Device, Data, State

admin.site.register(User, UserAdmin)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(State)
