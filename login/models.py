'''doc string'''
from django.db import models

# Create your models here.

"""
to check sql query it will fire run command python manage.py sqlmigrate
login 0001 and to commit that run python manage.py migrate
"""

#create super user by running python manage.py createsuperuser
#below line added to remove pylint error
#pylint:disable=invalid-name
class User(models.Model):
    '''doc string'''
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_gender = models.CharField(choices=( ('M', 'Male'), ('F', 'Female'), ), default='M', max_length=1)
    user_mobile = models.CharField(max_length=70, default="")
    user_image = models.ImageField(upload_to="login/userimage", default="")
    user_dob = models.DateField(null=True)
    user_description = models.CharField(max_length=300, default="")

    def __str__(self): # so that it displays email in admin objects
        return self.user_email
