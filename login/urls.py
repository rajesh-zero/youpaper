from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name="login"),
    path('test/', views.loguserin,name="loguserin"),
    path('register/', views.register,name="register"),
]
