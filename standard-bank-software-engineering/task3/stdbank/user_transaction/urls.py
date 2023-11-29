from django.urls import path

from . import views

urlpatterns = [
    path('some_info', views.get_some_info, name='index')
]
