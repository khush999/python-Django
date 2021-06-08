from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
      # path('', views.index, name="AdminPage"),
      path('flogin', views.flogin, name='flogin'),
      path('fregister', views.fregister, name='fregister'),
      path('reviewstudent', views.reviewstudent, name='reviewstudent'),
      path('flogout', views.flogout, name='flogout'),
]
