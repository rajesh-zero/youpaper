"""activity views.py"""
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist #to raise exception when record doesnot exist in table
from activity.models import Watched, Watchlist #importing models that i created in activity models.py
from login.models import User  #importing models that i created in login models.py
from ypdb.models import Ypdb #importing models that i created in ypdb models.py

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
    html_attributes = {} #creating dictionary to send as JSonResponse
    movie_id = request.GET['tid'] #getting movieid from url
    userid = request.session['user_id'] #getting user id from session that was set while logging in
    data_count = Watched.objects.filter(ypdb_id=movie_id, user_id=userid).count() #getting count of record is already exist it will be either 0 or 1
    if data_count == 0:#if 0 then add to database
        user = User.objects.get(user_id=userid)
        movie = Ypdb.objects.get(ypdb_id=movie_id)
        watched_object = Watched(user_id=user, ypdb_id=movie)
        watched_object.save()#inserting in table
        html_attributes['cssClass'] = 'ypdbactivity btn btn-success btn-block'#sending class information to set on page
        html_attributes['innerHTML'] = 'Remove Watched'
        return JsonResponse(html_attributes)
    elif data_count == 1:#else remove from database
        Watched.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-primary btn-block'
        html_attributes['innerHTML'] = 'Add to Watched'
        return JsonResponse(html_attributes)

def watch(request):
    """activity function"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    html_attributes = {} #creating dictionary to send as JSonResponse
    movie_id = request.GET['tid'] #getting movieid from url
    userid = request.session['user_id'] #getting user id from session that was set while logging in
    data_count = Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).count() #getting count of record is already exist it will be either 0 or 1
    if data_count == 0: #if 0 then add to database
        user = User.objects.get(user_id=userid)
        movie = Ypdb.objects.get(ypdb_id=movie_id)
        watchlist_object = Watchlist(user_id=user, ypdb_id=movie)
        watchlist_object.save() #inserting in table
        html_attributes['cssClass'] = 'ypdbactivity btn btn-success btn-block' #sending class information to set on page
        html_attributes['innerHTML'] = 'Remove Watch'
        return JsonResponse(html_attributes)
    elif data_count == 1: #else remove from database
        Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-primary btn-block'
        html_attributes['innerHTML'] = 'Add to Watched'
        return JsonResponse(html_attributes)
