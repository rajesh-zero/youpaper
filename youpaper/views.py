"""doc string"""
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    """doc string"""
    # home_data = {'session_email' : (request.session['user_email'])}
    # return render(request, 'home.html', home_data)
    return render(request, 'home.html',)
def contactus(request):
    '''doc string'''
    return HttpResponse("contact us")
def aboutus(request):
    '''doc string'''
    return HttpResponse("about us")
