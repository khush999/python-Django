from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('slogin', views.slogin, name='slogin'),
    path('sregister', views.sregister, name='sregister'),
    path('smyaccount', views.smyaccount, name='smyaccount'),
    path('appliedjob', views.appliedjob, name='appliedjob'),
    path('jobmatches', views.jobmatches, name='jobmatches'),
    path('slogout', views.slogout, name='slogout'),
]
