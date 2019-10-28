"""activity views.py"""
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from activity.models import Watched,Watchlist
from login.models import User
from ypdb.models import Ypdb

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
    movie_id = request.GET['tid']
    userid = request.session['user_id']
    #print(movie_id)
    try:
        data_count = Watched.objects.filter(ypdb_id=movie_id, user_id=userid).count()
        #print(data_count)
        if data_count == 0:
            user = User.objects.get(user_id=userid)
            movie = Ypdb.objects.get(ypdb_id=movie_id)
            watched_object = Watched(user_id=user, ypdb_id=movie)
            watched_object.save()
        elif data_count == 1:
            pass
        else:
            pass
    except ObjectDoesNotExist:
        print('does not exist')
    return HttpResponse("added to watched")

def removefromwatched(request):
    """remove from watched function"""
    movie_id = request.GET['tid']
    userid = request.session['user_id']
    #print(movie_id)
    try:
        #print(data_count)
        Watched.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
    except ObjectDoesNotExist:
        print('something wrong')
    return HttpResponse("Removed from watched")

def addtowatch(request):
    """add to watched function"""
    movie_id = request.GET['tid']
    userid = request.session['user_id']
    #print(movie_id)
    try:
        data_count = Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).count()
        #print(data_count)
        if data_count == 0:
            user = User.objects.get(user_id=userid)
            movie = Ypdb.objects.get(ypdb_id=movie_id)
            watchlist_object = Watchlist(user_id=user, ypdb_id=movie)
            watchlist_object.save()
        elif data_count == 1:
            pass
        else:
            pass
    except ObjectDoesNotExist:
        print('does not exist')
    return HttpResponse("added to Watchlist")

def removefromwatch(request):
    """remove from watched function"""
    movie_id = request.GET['tid']
    userid = request.session['user_id']
    #print(movie_id)
    try:
        #print(data_count)
        """https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models"""
        Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
    except ObjectDoesNotExist:
        print('something wrong')
    return HttpResponse("Removed from Watchlist")


