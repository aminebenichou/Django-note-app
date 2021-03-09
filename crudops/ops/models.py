from django.db import models

# Create your models here.
'''class Users (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)'''

class Notes (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    userid = models.IntegerField(default=0)