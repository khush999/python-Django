from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('contact',views.contact, name='contact'),

]    
    