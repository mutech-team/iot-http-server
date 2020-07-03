from django.urls import path
from . import views

urlpatterns = [
    path("obtain_data/<uuid:deviceid>/<str:datatype>/latest", views.obtain_data_latest),
    path("obtain_data/<uuid:deviceid>/<str:datatype>", views.obtain_data),
    path("save_state/", views.save_state),

]
