"""ypdb urls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeredirect, name="home redirect"),
    path('view/', views.view, name="get data in database"),
    path('results/', views.results, name="get data in database and display on search"),
]
