from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contato, name="contato"),
    path('index', views.index, name="index"),
]