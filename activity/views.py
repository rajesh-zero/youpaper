"""activity views.py"""
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def activity(request):
    """activity function"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    return HttpResponse("activity page")
