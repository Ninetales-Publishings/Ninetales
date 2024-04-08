# from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class PubishedBooks(models.Model):
    BookFile = models.FileField(upload_to='bookCover(ForPublishedBooks)/',default=None,null=True)
    BookName = models.CharField(max_length=40,default="book",null= False)
    Writername = models.CharField(max_length=500,default="writer",null= False)
    BookFormat = models.CharField(max_length=500,default="paperback",null= False)
    Pages = models.IntegerField(default=0,null=False)
    ISBNNo = models.CharField(max_length=40,default="user",null= False)
    AboutBook = models.TextField(default="aboutBook",null=False)
    AboutAuthor = models.TextField(default="aboutAuthor",null=False)
    DOIDetail = models.CharField(max_length=40,default="user",null= True)


class PubishRequests(models.Model):
    BookName = models.CharField(max_length=40,default="book",null= False)
    Writername = models.CharField(max_length=500,default="user",null= False)
    Address = models.TextField(default=None,null=False)
    MainFile = models.FileField(upload_to='PublishRequests/MainFile',default=None,null=True)
    AuthorProfile = models.FileField(upload_to='PublishRequests/AuthorProfile',default=None,null=True)
    OtherFile = models.FileField(upload_to='PublishRequests/OtherFile',default=None,null=True)
    Message = models.TextField(default=None,null=True)
    Date_time = models.DateTimeField(null=True)

class MailRequest(models.Model):
    Email = models.CharField(max_length=40,default="userMail",null= False)
    Date_time = models.DateTimeField(null=True)