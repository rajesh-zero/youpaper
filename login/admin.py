'''doc string'''
from django.contrib import admin
from .models import users # imported users table from model
# Register your models here.

admin.site.register(users) #registered my table user to admin
