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
    #page_data = Watched.objects.select_related('ypdb_id').filter(user_id=request.session['user_id'])
    '''https://stackoverflow.com/questions/43772163/how-to-join-3-tables-in-query-with-django'''
    params = {}
    data = Watched.objects.select_related().filter(user_id=request.session['user_id'])
    watched_data = []
    for i in data:
        watched_data.append({'watched_id':i.watched_id, 'user_id':i.user_id.user_id, 'ypdb_id':i.ypdb_id.ypdb_id, 'ypdb_title':i.ypdb_id.ypdb_title})
    params['watched_data'] = watched_data #adding these data in params dictionary

    data = Watchlist.objects.select_related().filter(user_id=request.session['user_id'])
    watchlist_data = []
    for i in data:
        watchlist_data.append({'watchlist_id':i.watchlist_id, 'user_id':i.user_id.user_id, 'ypdb_id':i.ypdb_id.ypdb_id, 'ypdb_title':i.ypdb_id.ypdb_title})
    params['watchlist_data'] = watchlist_data #adding these data in params dictionary
    return render(request, 'activity/activity.html', params)

def watchedlist(request):
    """load watchedlist page"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    params = {}
    '''https://stackoverflow.com/questions/43772163/how-to-join-3-tables-in-query-with-django'''
    data = Watched.objects.select_related().filter(user_id=request.session['user_id'])
    watched_data = []
    for i in data:
        watched_data.append({'watched_id':i.watched_id, 'user_id':i.user_id.user_id, 'ypdb_id':i.ypdb_id.ypdb_id, 'ypdb_title':i.ypdb_id.ypdb_title})
    params['watched_data'] = watched_data #adding these data in params dictionary
    return render(request, 'activity/watchedlist.html',params)

def watchlist(request):
    """load watchlist page"""
    if request.session['user_email'] == '':
        return redirect('/login/')
    params = {}
    '''https://stackoverflow.com/questions/43772163/how-to-join-3-tables-in-query-with-django'''
    data = Watchlist.objects.select_related().filter(user_id=request.session['user_id'])
    watchlist_data = []
    for i in data:
        watchlist_data.append({'watchlist_id':i.watchlist_id, 'user_id':i.user_id.user_id, 'ypdb_id':i.ypdb_id.ypdb_id, 'ypdb_title':i.ypdb_id.ypdb_title})
    params['watchlist_data'] = watchlist_data #adding these data in params dictionary
    return render(request, 'activity/watchlist.html',params)

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
    if data_count == 1:#else remove from database
        Watched.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-primary btn-block'
        html_attributes['innerHTML'] = 'Add to Watched'
        return JsonResponse(html_attributes)
    '''https://stackoverflow.com/questions/41631822/return-a-variable-vs-return-a-function-call'''
    return HttpResponse('<h1>somethings wrong</h1>')

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
        html_attributes['innerHTML'] = 'Remove Watchlist'
        return JsonResponse(html_attributes)
    if data_count == 1: #else remove from database
        Watchlist.objects.filter(ypdb_id=movie_id, user_id=userid).delete()
        html_attributes['cssClass'] = 'ypdbactivity btn btn-primary btn-block'
        html_attributes['innerHTML'] = 'Add to Watchlist'
        return JsonResponse(html_attributes)
    return HttpResponse('<h1>somethings wrong</h1>')
