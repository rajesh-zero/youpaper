"""ypdb urls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeredirect, name="home redirect"),
]
