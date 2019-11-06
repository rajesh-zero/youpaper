"""doc string"""
import json
import requests
from django.shortcuts import render, redirect
from django.core.paginator import Paginator#for pagination
from django.http import HttpResponse
from django.db.models import Q #to use ~Q to do negation
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
    datas = Ypdb.objects.filter(~Q(ypdb_poster='N/A')).order_by('-ypdb_id')[:100]#to get only last 20records with images in descending order
    #print(datas)
    paginator = Paginator(datas, 12) # Show 25 contacts per page
    page = request.GET.get('page')
    data = paginator.get_page(page)

    params = {'datas':data, 'range':range(6)}
    print(params['datas'])
    return render(request, 'home.html', params)
def contactus(request):
    '''doc string'''
    return HttpResponse("contact us")
def aboutus(request):
    '''doc string'''
    return HttpResponse("about us")