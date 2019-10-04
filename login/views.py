'''views.py for login '''
from django.shortcuts import render
from django.http import HttpResponse
from login.models import users
# Create your views here.

# def login(request):
#     return HttpResponse("login page")
def login(request):
    '''
    stupid thing to disable pylint warning
    '''
    return render(request, 'login/login.html')


def register(request):
    '''
    stupid thing to disable pylint warning
    '''
    return render(request, 'login/register.html')


def loguserin(request):
    '''
    stupid thing to disable pylint warning
    '''
    emailid = request.POST.get('email')
    password = request.POST.get('password')
    user_data = users.objects.get(user_email=emailid) 
    #here was an error for that install pip install pylint-django
    if user_data.user_password == password:
        return HttpResponse("login successful")
    return render(request, 'userprofile/profile.html', {'email': emailid, 'password':password}) 
    # calling profile page of userprofile application

# def registered(request):
    # emailid = request.POST.get('email','mera mail')    #this is also valid
    # password = request.POST.get('password','mera mail')   
    # password = request.POST.get('name')
    # return render(request,'login/register.html',{'register':"registered"})
def registered(request):
    '''
    stupid thing to disable pylint warning
    '''
    if request.method == 'POST':
        emailid = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if emailid != '' and password != '':
            user = users(user_email=emailid, user_password=password, user_name=name)
            user.save()
            return HttpResponse("<script>alert('registered successfully')</script>")
    return HttpResponse("<script>alert('something went wrong')</script>")
    