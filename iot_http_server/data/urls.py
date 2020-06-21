from django.urls import path
from . import views

urlpatterns = [
    path("obtain/<uuid:deviceid>/<str:datatype>/latest", views.obtain_data_latest),
    path("obtain/<uuid:deviceid>/<str:datatype>", views.obtain_data),

]
