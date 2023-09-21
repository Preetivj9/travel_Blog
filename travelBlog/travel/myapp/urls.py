from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('index/',views.index,name="index"),
    path('user_data/',views.user_dat,name='user_data')
]
