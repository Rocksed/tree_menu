from django.urls import path

from django_app import views
from django_app.apps import DjangoAppConfig


app_name = DjangoAppConfig.name

urlpatterns = [
    path('', views.menu_list, name='menu')
]

