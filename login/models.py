from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=1,default="")
    user_mobile = models.CharField(max_length=70, default="")
    user_dob = models.DateField()
    user_description = models.CharField(max_length=300,default="")

    

