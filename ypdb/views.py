"""ypdb.py for login """
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ypdb.models import Ypdb
from login.models import User
from activity.models import Watchlist, Watched
from codes.apimethods import search_api
# Create your views here.

def homeredirect(request):
    """homeredirect function"""
    return render(request, 'ypdb/insert.html')

def view(request):
    """homeredirect function"""
    title = request.GET['t']
    movie_id = request.GET['id']
    plot = 'full' #to get full description of plot
    header = {'t': title, 'plot':plot}
    parseddata = search_api(header)#passing header
    params = {'datas':parseddata}
    #print(parseddata)
    ypdb = Ypdb.objects.get(ypdb_id=movie_id)
    ypdb.ypdb_genre = parseddata['Genre']
    ypdb.ypdb_plot = parseddata['Plot']
    ypdb.ypdb_runtime = parseddata['Runtime']
    if 'totalSeasons' in parseddata:
        """this if checks if there is totalseason or not in parseddata"""
        ypdb.ypdb_seasons = parseddata['totalSeasons']
    ypdb.save()
    """https://stackoverflow.com/questions/6253611/how-to-get-the-id-of-the-record-just-saved"""
    params['ypdb_id'] = movie_id
    #print(params)
    user = User.objects.get(user_id=request.session['user_id'])
    watched_status = Watched.objects.filter(user_id=user, ypdb_id=movie_id).count()
    watchlist_status = Watchlist.objects.filter(user_id=user, ypdb_id=movie_id).count()
    print(watched_status, watchlist_status)
    params['watched_status'] = watched_status
    params['watchlist_status'] = watchlist_status
    #print(params)
    return render(request, 'ypdb/view.html', params)

def results(request):
    """homeredirect function"""
    search = request.GET['search'] #getting search terms from user
    header = {'s': search}
    parseddata = search_api(header)
    params = {}
    listparsed = [] #for this to be available outside if
    if parseddata['Response'] == 'True':
        listparsed = parseddata['Search'] #filtering search dictionary that contains list of dictionary
        for enum in enumerate(listparsed):
            #print(enum[1])#iterating through enum tuple and selecting values
            #proud of below try catch and if elif  made very short logic instead of before insertdb
            #below logic checks if movie exist in db if yes then skips else adds in db
            try:
                if Ypdb.objects.filter(ypdb_title=enum[1]['Title']).count() == 1:
                    continue
                elif enum[1]['Poster'] != 'N/A':
                    records_to_insert = Ypdb(ypdb_title=enum[1]['Title'], ypdb_year=enum[1]['Year'], ypdb_type=enum[1]['Type'],        ypdb_poster=enum[1]['Poster'])
                    records_to_insert.save()
            except Ypdb.DoesNotExist:
                pass
        #below line does search in database to get result
        #https://docs.djangoproject.com/en/1.11/ref/models/querysets/#startswith
        datas = Ypdb.objects.filter(ypdb_title__icontains=search)
        params = {'datas':datas}
    return render(request, 'ypdb/results.html', params)
    