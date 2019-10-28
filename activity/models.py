"""activity model.py file"""
from django.db import models
from login.models import User
from ypdb.models import Ypdb

# Create your models here.
class Watched(models.Model):
    """class for watched stuff"""
    watched_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ypdb_id = models.ForeignKey(Ypdb, on_delete=models.CASCADE)

class Watchlist(models.Model):
    """class for watched stuff"""
    watchlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ypdb_id = models.ForeignKey(Ypdb, on_delete=models.CASCADE)
