"""activity views.py"""
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from activity.models import Watched, Watchlist
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
    html_attributes = {}
    movie_id = request.GET['tid']
    userid = request.session['user_id']
    data_count = Watched.objects.filter(ypdb_id=movie_id, user_id=userid).count()
    if data_count == 0:
        user = User.objects.get(user_id=userid)
        movie = Ypdb.objects.get(ypdb_id=movie_id)
        watched_object = Watched(user_id=user, ypdb_id=movie)
        watched_object.save()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-success btn-block'
        html_attributes['innerHTML'] = 'Remove Watched'
        return JsonResponse(html_attributes)
    elif data_count == 1:
        Watched.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-primary btn-block'
        html_attributes['innerHTML'] = 'Add to Watched'
        return JsonResponse(html_attributes)

def watch(request):
    """activity function"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    html_attributes = {}
    movie_id = request.GET['tid']
    userid = request.session['user_id']
    data_count = Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).count()
    if data_count == 0:
        user = User.objects.get(user_id=userid)
        movie = Ypdb.objects.get(ypdb_id=movie_id)
        watchlist_object = Watchlist(user_id=user, ypdb_id=movie)
        watchlist_object.save()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-success btn-block'
        html_attributes['innerHTML'] = 'Remove Watch'
        return JsonResponse(html_attributes)
    elif data_count == 1:
        Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-primary btn-block'
        html_attributes['innerHTML'] = 'Add to Watched'
        return JsonResponse(html_attributes)
