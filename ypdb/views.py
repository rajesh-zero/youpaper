"""ypdb.py for login """
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ypdb.models import Ypdb
from codes.apimethods import search_api
# Create your views here.

def homeredirect(request):
    """homeredirect function"""
    return render(request, 'ypdb/insert.html')
def view(request):
    """homeredirect function"""
    title = request.GET['t']
    print(title)
    return render(request, 'ypdb/view.html')

def results(request):
    """homeredirect function"""
    search = request.GET['search'] #getting search terms from user
    parseddata = search_api(search)
    params = {}
    listparsed = [] #for this to be available outside if
    if parseddata['Response'] == 'True':
        listparsed = parseddata['Search'] #filtering search dictionary that contains list of dictionary
        for enum in enumerate(listparsed):
            #print(enum[1])#iterating through enum tuple and selecting values
            try:
                if Ypdb.objects.filter(ypdb_title=enum[1]['Title']).count() == 1:
                    continue
                elif enum[1]['Poster'] != 'N/A':
                    records_to_insert = Ypdb(ypdb_title=enum[1]['Title'], ypdb_year=enum[1]['Year'], ypdb_type=enum[1]['Type'],        ypdb_poster=enum[1]['Poster'])
                    records_to_insert.save()
            except Ypdb.DoesNotExist:
                pass

        params = {'datas':listparsed}
    return render(request, 'ypdb/results.html', params)

def insertindb(request):
    """insertinDB function"""
    search = request.GET['search']
    parseddata = search_api(search)
    if parseddata['Response'] is False:
        print(parseddata['Response'])
        return HttpResponse('<h1>not found</h1>')
    else:
        listparsed = parseddata['Search']
        for i in range(0,len(listparsed)):
            datadictionary = {}
            data_count = 0
            for key,value in listparsed[i].items():
                if key == 'imdbID':
                    continue
                datadictionary[key] = value
            #print(datadictionary)
            try:
                data_count = Ypdb.objects.filter(ypdb_title=datadictionary['Title']).count()
                print(datadictionary['Title']," ", data_count)
                if data_count == 1:
                    continue
                else:
                    ypdb = Ypdb(ypdb_title=datadictionary['Title'], ypdb_year=datadictionary['Year'], ypdb_type=datadictionary['Type'],       ypdb_poster=datadictionary['Poster'])
                    ypdb.save()
            except Ypdb.DoesNotExist:
                pass
    return redirect("/ypdb/")
