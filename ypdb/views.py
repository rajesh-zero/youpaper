"""ypdb.py for login """
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def homeredirect(request):
    """homeredirect function"""
    return HttpResponse("<script>alert('ypdp home page')</script>")
    #return render(request, 'login/test.html')
