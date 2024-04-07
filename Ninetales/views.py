import datetime

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Feedback.models import *
from Publish.models import *

from .settings import MEDIA_URL


def index(request):
    books = PubishedBooks.objects.all()[:5]
    try:
        if request.method == 'POST':
            name = request.POST.get("fullName")
            email = request.POST.get("Email")

            data = subscribers(name = name, email = email,date_time = datetime.datetime.now())
            data.save()
            return render(request,"index.html",{"MEDIA_URL":MEDIA_URL,"books" : books,"message" : "Subscribed!!"})
    except:
        pass
    return render(request,"index.html",{"MEDIA_URL":MEDIA_URL,"books" : books})

def feedbackPage(request):

    try:
        if request.method == 'POST':
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("umail")
            phno = request.POST.get("phno")
            cntry = request.POST.get("cntry")
            uaddress = request.POST.get("uaddress")
            content = request.POST.get("content")
            print(datetime.datetime.now())
            data = feedback(fname = fname,lname = lname,email = email,mobileNo = phno,country = cntry,address = uaddress,feedback = content,date_time = datetime.datetime.now())
            data.save()

            return render(request,"feedback.html",{"message" : "Thank You!"})
    except:
        pass

    return render(request,"feedback.html")


def contactUs(request):

    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            phno = request.POST.get("phno")
            enquiry = request.POST.get("enquiry")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            Query = {
                "Query1" : "Submission Queries",
                "Query2" : "Press and Marketing Enquiries",
                "Query3" : "General Enquiries",
            }

            data = queries(name = name, email = email,mobileNo = phno,query = Query[enquiry],subject = subject, message = message, date_time = datetime.datetime.now())
            data.save()
            return render(request,"contactUs.html",{"message" : "Query Received"})
    except:
        pass

    return render(request,"contactUs.html")

def submitBook(request):

    try:
        if request.method == 'POST':
            bookName = request.POST.get("bookName");
            writerName = request.POST.get("writerName");
            address = request.POST.get("address");
            mainFile = request.FILES["mainFile"];
            authorProfile = request.FILES["authorProfile"];
            otherFile = request.FILES["otherFile"];
            message = request.POST.get("message");

            book = PubishRequests(BookName = bookName, Writername = writerName,Address = address,MainFile = mainFile,AuthorProfile = authorProfile,OtherFile = otherFile,Message = message,Date_time = datetime.datetime.now())
            book.save()

            return render(request,"submitBook.html",{"message" : "Success"})
    except:
        pass

    return render(request,"submitBook.html")

def aboutUs(request):

    return render(request,"aboutUs.html")

def faq(request):

    return render(request,"faq.html")

def books(request):
    try:
        books = PubishedBooks.objects.all()
        return render(request,"books.html",{"MEDIA_URL":MEDIA_URL,"topbooks":books[:5],"books":books})
    except:
        pass
    
    return render(request,"books.html")

def book(request,bookName):
    try:
        book = PubishedBooks.objects.get(BookName = bookName)
        return render(request,"book.html",{"MEDIA_URL":MEDIA_URL,"book":book})
    except:
        pass
    
    return render(request,"book.html")