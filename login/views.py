from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def login(request):
#     return HttpResponse("login page")
def login(request):
    return render(request,'login/login.html')
def register(request):
    return render(request,'login/login.html')
def loguserin(request):
    
    emailid = request.POST['email']     #This is valid
    #emailid = request.POST.get('email','mera mail')    #this is also valid
    password = request.POST['password']
    rememberme = request.POST.get('remember','off') # returns 0n or off for checkbox by default
    print(emailid," ",password," ",rememberme)

    return render(request,'login/test.html',{'email':emailid,'password':password})