"""views.py for login """
from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
# Create your views here.

def login(request):
    """
    stupid thing to disable pylint warning
    """
    return render(request, 'login/login.html')


def register(request):
    """
    stupid thing to disable pylint warning
    """
    return render(request, 'login/register.html')


def loguserin(request):
    """
    this method checks user name and password and logs user in
    """
    """
    there was an error for that install pip install pylint-django
    """
    emailid = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user_data = User.objects.get(user_email=emailid)
    except User.DoesNotExist:
        return HttpResponse("<script>alert('User not found')</script>")


    if user_data.user_password == password:
        return HttpResponse("login successful")
    return HttpResponse("<script>alert('something went wrong')</script>")

    #return render(request, 'userprofile/profile.html', {'email': emailid, 'password':password}) 
    # calling profile page of userprofile application

def registered(request):
    """
    This method registers user in database
    """
    if request.method == 'POST':
        emailid = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if emailid != '' and password != '':
            user = User(user_email=emailid, user_password=password, user_name=name)
            user.save()
            return HttpResponse("<script>alert('registered successfully')</script>")
    return HttpResponse("<script>alert('something went wrong')</script>")
    