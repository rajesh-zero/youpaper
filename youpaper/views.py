"""doc string"""
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    """doc string"""
    return render(request, 'home.html',)
def contactus(request):
    '''doc string'''
    return HttpResponse("contact us")
def aboutus(request):
    '''doc string'''
    return HttpResponse("about us")
