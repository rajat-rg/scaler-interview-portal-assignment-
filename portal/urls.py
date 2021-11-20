from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('upcoming', views.upcoming, name='upcoming'),
]