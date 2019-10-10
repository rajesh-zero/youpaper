"""doc string"""
from django.contrib import admin
from .models import Ypdb, Watched

# Register your models here.

admin.site.register(Ypdb)
admin.site.register(Watched)
