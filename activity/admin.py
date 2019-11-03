"""activity admin.py file"""
from django.contrib import admin
from .models import Watched, Watchlist

# Register your models here.

admin.site.register(Watched)
admin.site.register(Watchlist)
