"""userprofile views.py file"""
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myprofile(request):
    """returns profile page"""
    return render(request, 'userprofile/profile.html')
