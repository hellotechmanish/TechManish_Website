# from django.contrib import admin
from django.urls import  path
# from os import path
from manish_world import views



urlpatterns = [

    path('manishworld', views.home1, name='home1'),
]