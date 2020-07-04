from django.urls import path
from . import views


urlpatterns = [
    path("obtain_data/<uuid:deviceid>/<str:datatype>/latest", views.obtain_data_latest),
    path("obtain_data/<uuid:deviceid>/<str:datatype>", views.obtain_data),
    path("obtain_data/<uuid:deviceid>/", views.obtain_data_all),
    path("obtain_state/<uuid:deviceid>/<str:statetype>", views.obtain_state),
    path("obtain_states/<uuid:deviceid>/", views.obtain_state_all),
    path("save_state/", views.save_state),
]
