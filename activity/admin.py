"""activity admin.py file"""
from django.contrib import admin
from .models import Watched

# Register your models here.

admin.site.register(Watched)
