# posts/urls.py
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/',views.groups_posts,name = 'group')
] 