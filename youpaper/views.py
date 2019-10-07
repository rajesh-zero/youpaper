"""doc string"""
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from ypdb.models import Ypdb
# Create your views here.

def home(request):
    """doc string"""
    if request.session['user_email']:
        print('if ke andhar hai')
    else:
        request.session['user_email'] = ''
    datas = Ypdb.objects.filter(~Q(ypdb_poster='N/A'))#to get only records with images
    print(type(datas))
    params = {'datas':datas, 'range':range(6)}
    return render(request, 'home.html', params)
def contactus(request):
    '''doc string'''
    return HttpResponse("contact us")
def aboutus(request):
    '''doc string'''
    return HttpResponse("about us")
def insertindb(request):
    '''doc string'''
    search = request.GET['search']
    headers = {}
    headers['s'] = search
    headers['apikey'] = '16ee2b99'
    req = requests.get('http://www.omdbapi.com/?', params=headers)
    parseddata = json.loads(req.text)
    print('***************************', parseddata['Response'])
    print(parseddata['Response'] is True)
    response = parseddata['Response']
    if response == 'True':
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
        return HttpResponse('<h1>successful</h1>')
    elif response == 'False':
        return HttpResponse("<h1>not found</h1>")
    else:
        return HttpResponse("<h1>something wrong</h1>")
