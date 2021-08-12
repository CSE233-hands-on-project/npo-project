from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def home(http_req):
    return render(http_req, 'login.html')


def guest(http_req):
    return HttpResponse("Everybody is welcome here!")


def registered(http_req):
    return HttpResponse("You must be registered to see this page!")


def administrator(http_req):
    return HttpResponse("You must be an administrator to see this page!")


# The child paths of the root page
urlpatterns = [
    path('', home),  # the base URL (no child)
    path('g/', guest),
    path('r/', registered),
    path('a/', administrator),  # path('admin/', admin.site.urls)
]
