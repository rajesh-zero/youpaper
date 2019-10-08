"""ypdb urls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeredirect, name="home redirect"),
    path('insertindb/', views.insertindb, name="get data in database"),
    path('view/', views.view, name="get data in database"),
]
