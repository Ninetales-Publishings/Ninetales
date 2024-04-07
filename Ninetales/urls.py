"""
URL configuration for Ninetales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = "Ninetales Publishers"
admin.site.site_title = "Welcome to Ninetales"
admin.site.index_title = "Welcome to Ninetales"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "home"),
    path('feedback', views.feedbackPage,name = "feedback"),
    path('contactUs', views.contactUs,name = "contactUs"),
    path('submitBook', views.submitBook,name = "submitBook"),
    path('aboutUs', views.aboutUs,name = "aboutUs"),
    path('faq', views.faq,name = "faq"),
    path('books', views.books,name = "books"),
    path('books/<str:bookName>', views.book,name = "book"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)