from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.WeatherView.as_view(), name='index'),
    path('delete/<pk>/', views.delete_location, name='delete')
]
