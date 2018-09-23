from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    usertype = models.CharField(max_length=2)
    password = models.CharField(max_length=50)
