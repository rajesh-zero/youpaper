"""activity views.py"""
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def activity(request):
    """activity function"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    return render(request, 'activity/activity.html')

def watched(request):
    """activity function"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    return HttpResponse("watched page")

def watch(request):
    """activity function"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    return HttpResponse("watch page")

def addtowatched(request):
    """add to watched function"""
    return True

def addtowatch(request):
    """add to watch function"""
    return True

def removefromwatched(request):
    """remove from watched function"""
    return True

def removefromwatch(request):
    """remove from watch function"""
    return True
