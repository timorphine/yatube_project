from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('groups/', views.group_posts),
    path('groups/<slug:slug>/', views.group_posts_details),
] 