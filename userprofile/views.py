"""userprofile views.py file"""
from django.shortcuts import render
from . import views
# Create your views here.

def myprofile(request):
    return render(request,'userprofile/profile.html')