from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('superuser', views.superuser, name='superuser'),
    path('topic', views.topic, name='topic'),
    path('test_setup', views.test_setup, name='test_setup'),
    path('test_teardown', views.test_teardown, name='test_teardown'),
]
