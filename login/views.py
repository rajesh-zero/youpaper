"""views.py for login """
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from login.models import User
from login.forms import UserForm
# Create your views here.

def login(request):
    """
    takes you to login page
    """
    if request.session['user_email'] != '':
        return redirect('/')
    return render(request, 'login/login.html')

def logout(request):
    """logout function"""
    request.session['user_email'] = ''
    return redirect('/')

def test(request):
    """test function"""
    x = request.GET['post_id']
    y = request.GET['test_id']
    #return render(request, 'login/test.html')
    return HttpResponse("Success!"+x+y)
    
def profile(request):
    """profile page function"""
    params = {}
    try:
        user_data = User.objects.get(user_email=request.session['user_email'])
        params = {'data':user_data}
    except User.DoesNotExist:
        pass
    return render(request, 'login/profile.html', params)


def register(request):
    """
    takes you to register page
    """
    if request.session['user_email'] != '':
        return redirect('/')
    return render(request, 'login/register.html')

def updateprofile(request):
    """
    takes you to updateprofile page
    """
    if request.session['user_email'] != '':
        try:
            user = User.objects.get(user_email=request.session['user_email'])
            form = UserForm(initial={'user_id':user.user_id, 'user_name': user.user_name, 'user_email': user.user_email, 'user_mobile': user.user_mobile, 'user_dob': user.user_dob, 'user_description': user.user_description, 'user_password':user.user_password,'user_gender':user.user_gender})
        except User.DoesNotExist:
            return HttpResponse("sorry") 
        if form.is_valid():
            form.save()
        return render(request, 'login/updateprofile.html', {'forms':form})
    return render(request, 'login/register.html')


def updateuserdata(request):
    """
    takes you to updateprofile page
    """
    if request.session['user_email'] != '':
        form = UserForm(request.POST or None)
        if form.is_valid():
            try:
                user = User.objects.get(user_email=request.session['user_email'])
                user.user_email = request.POST.get('user_email').lower().strip()
                user.user_name = request.POST.get('user_name').strip()
                user.user_gender = request.POST.get('user_gender')
                dob = request.POST.get('user_dob_year')+"-"+request.POST.get('user_dob_month')+"-"+request.POST.get('user_dob_day')
                user.user_dob = dob
                user.user_description = request.POST.get('user_description')
                user.user_mobile = request.POST.get('user_mobile')
                user.save()
            except User.DoesNotExist:
                return HttpResponse("sorry")
        # if form.is_valid():
        #     form.save()
        messages.info(request, 'Updated successfully!')
        return redirect('/login/updateprofile/')
    return HttpResponse("<script>alert('Failed')</script>")

def loguserin(request):
    """
    this method checks user name and password and logs user in
    """
    """
    there was an error for that install pip install pylint-django
    """
    emailid = request.POST.get('email').lower().strip()
    password = request.POST.get('password').strip()
    try:
        user_data = User.objects.get(user_email=emailid)
        print(user_data)
        if user_data.user_password == password:
            request.session['user_email'] = emailid
            request.session['user_id'] = user_data.user_id
            return redirect('/')
        messages.info(request, 'username or password incorrect')
        return HttpResponseRedirect('/login/')
        #return HttpResponse("<script>alert('username or password incorrect')</script>")
    except User.DoesNotExist:
        messages.info(request, 'user not found')
        return HttpResponseRedirect('/login/')
        #return HttpResponse("<script>alert('User not found')</script>")

    #return render(request, 'userprofile/profile.html', {'email': emailid, 'password':password})
    # calling profile page of userprofile application

def registered(request):
    """
    This method registers user in database
    """
    if request.method == 'POST':
        emailid = request.POST.get('email').lower().strip()
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()
        try:
            data_count = User.objects.filter(user_email=emailid).count()
            if data_count == 1:
                #return HttpResponse("<script>alert('email already exist')</script>")
                messages.info(request, 'email already exist')
                return HttpResponseRedirect('/login/register/')
            else:
                if emailid != '' and password != '':
                    user = User(user_email=emailid, user_password=password, user_name=name)
                    user.save()
                    messages.info(request, 'Registered successfully! Login to continue')
                    return HttpResponseRedirect('/login/')
                    #return HttpResponse("<script>alert('registered successfully')</script>")
                else:
                    #return HttpResponse("<script>alert('something went wrong')</script>")
                    messages.info(request, 'something went wrong try again')
                    return HttpResponseRedirect('/login/register/')
        except User.DoesNotExist:
            pass
    #return HttpResponse("<script>alert('something went wrong')</script>")
    messages.info(request, 'something went wrong try again')
    return HttpResponseRedirect('/login/register/')
    