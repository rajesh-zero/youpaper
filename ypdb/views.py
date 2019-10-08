"""ypdb.py for login """
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ypdb.models import Ypdb
# Create your views here.

def homeredirect(request):
    """homeredirect function"""
    return render(request, 'ypdb/insert.html')
def view(request):
    """homeredirect function"""
    return render(request, 'ypdb/view.html')

def insertindb(request):
    """insertinDB function"""
    search = request.GET['search']
    headers = {}
    headers['s'] = search
    headers['apikey'] = '16ee2b99'
    req = requests.get('http://www.omdbapi.com/?', params=headers)
    parseddata = json.loads(req.text)
    if parseddata['Response'] is False:
        print(parseddata['Response'])
        return HttpResponse('<h1>not found</h1>')
    else:
        listparsed = parseddata['Search']
        print(headers)
        print(req.status_code)
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
