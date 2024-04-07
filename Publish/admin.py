from django.contrib import admin

# Register your models here.
from Publish.models import *


class admin_PubishedBooks(admin.ModelAdmin):
    list_display = ("BookFile","BookName","Writername","ISBNNo","Abstract","DOIDetail")

admin.site.register(PubishedBooks,admin_PubishedBooks)

class admin_PubishRequests(admin.ModelAdmin):
    list_display = ("BookName","Writername","Address","MainFile","AuthorProfile","OtherFile","Message","Date_time")

admin.site.register(PubishRequests,admin_PubishRequests)