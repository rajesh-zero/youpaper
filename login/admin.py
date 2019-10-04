"""doc string"""
from django.contrib import admin
from .models import User # imported users table from model
# Register your models here.

admin.site.register(User) #registered my table user to admin
