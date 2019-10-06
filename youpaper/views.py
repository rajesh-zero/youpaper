"""doc string"""
from django.shortcuts import render
from django.http import HttpResponse
from ypdb.models import Ypdb
# Create your views here.

def home(request):
    """doc string"""
    datas = Ypdb.objects.filter(ypdb_poster__isnull=False)
    print(datas)
    params = {'datas':datas, 'range':range(6)}
    return render(request, 'home.html', params)
def contactus(request):
    '''doc string'''
    return HttpResponse("contact us")
def aboutus(request):
    '''doc string'''
    return HttpResponse("about us")
