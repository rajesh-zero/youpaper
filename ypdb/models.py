"""ypdb models.py"""
from django.db import models
from login.models import User

# Create your models here.
class Ypdb(models.Model):
    """Ypdb class"""
    ypdb_id = models.AutoField(primary_key=True)
    ypdb_title = models.CharField(max_length=100)
    ypdb_year = models.CharField(max_length=50, default="")
    ypdb_type = models.CharField(max_length=50, default="")
    ypdb_poster = models.CharField(max_length=300, default="")  

    def __str__(self): # so that it displays email in admin objects
        return self.ypdb_title

class Watched(models.Model):
    """class for watched stuff"""
    watched_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ypdb_id = models.ForeignKey(Ypdb, on_delete=models.CASCADE)
