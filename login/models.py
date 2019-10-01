from django.db import models

# Create your models here.

# to check sql query it will fire run command python manage.py sqlmigrate login 0001 and to commit that run python manage.py migrate
#create super user by running python manage.py createsuperuser ( I created username = admin, email = admin@email.com , password = admin123)
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=1,default="")
    user_mobile = models.CharField(max_length=70, default="")
    user_dob = models.DateField()
    user_description = models.CharField(max_length=300,default="")




    

