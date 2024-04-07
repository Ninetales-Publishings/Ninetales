from django.db import models


# Create your models here.
class feedback(models.Model):
    fname = models.CharField(max_length=40,default="user",null= False)
    lname = models.CharField(max_length=40,default="user",null= False)
    mobileNo = models.CharField(max_length=20,default="user",null= False)
    address = models.TextField(default=None,null=False)
    email = models.EmailField(default=None, null= False , max_length = 320)
    country = models.CharField(max_length=10,default="India",null = False)
    feedback = models.TextField(default=None,null = False)
    date_time = models.DateTimeField(null=True)

class queries(models.Model):
    name = models.CharField(max_length=40,default="user",null= False)
    email = models.EmailField(default=None, null= False , max_length = 320)
    mobileNo = models.CharField(max_length=20,default="user",null= False)
    query = models.CharField(max_length=40,default="Query",null = False)
    subject = models.CharField(max_length=40,default="Subject",null = False)
    message = models.TextField(default=None,null=False)
    date_time = models.DateTimeField(null=True)

class subscribers(models.Model):
    name = models.CharField(max_length=40,default="user",null= False)
    email = models.EmailField(default=None, null= False , max_length = 320)
    date_time = models.DateTimeField(null=True)