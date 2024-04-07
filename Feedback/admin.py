from django.contrib import admin

# Register your models here.
from Feedback.models import *


class admin_feedback(admin.ModelAdmin):
    list_display = ("fname","lname","mobileNo","address","email","country","feedback","date_time")

admin.site.register(feedback,admin_feedback)

class admin_queries(admin.ModelAdmin):
    list_display = ("name","email","mobileNo","query","subject","message","date_time")

admin.site.register(queries,admin_queries)

class admin_subscribers(admin.ModelAdmin):
    list_display = ("name","email","date_time")

admin.site.register(subscribers,admin_subscribers)