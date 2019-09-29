from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')
# def home(request):
#     return HttpResponse("home")
def contactus(request):
    return HttpResponse("contact us")
def aboutus(request):
    return HttpResponse("about us")