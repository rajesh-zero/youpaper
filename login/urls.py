"""login urls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logged/', views.loguserin, name="loguserin"),
    path('logout/', views.logout, name="loguserin"),
    path('register/', views.register, name="register"),
    path('registered/', views.registered, name="registered"),
    path('test/', views.test, name="test"),
    path('profile/', views.profile, name="profile"),
]
