"""doc string"""
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from ypdb.models import Ypdb
from codes.apimethods import search_api
# Create your views here.

def home(request):
    """doc string"""
    try:
        xox = request.session['user_email']
        print("..................", xox, "...........Loaded home page")
    except KeyError:
        request.session['user_email'] = ''
    # if request.session['user_email']:
    #     print('if ke andhar hai')
    # else:
    #     request.session['user_email'] = ''
    datas = Ypdb.objects.filter(~Q(ypdb_poster='N/A')).order_by('-ypdb_id')[:20]#to get only last 20records with images in descending order
    #print(datas)
    params = {'datas':datas, 'range':range(6)}
    return render(request, 'home.html', params)
def contactus(request):
    '''doc string'''
    return HttpResponse("contact us")
def aboutus(request):
    '''doc string'''
    return HttpResponse("about us")
