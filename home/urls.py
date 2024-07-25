from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.coverpage, name='coverpage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contacts'),
    path('vWorld', views.vWorld, name='vWorld'),
    path('avatar', views.avatar, name='avatar'),
    path('community', views.community, name='community'),
    path('therapist', views.therapist, name='therapist'),
    path('assessment', views.assessment, name='assessment'),
    path('resources', views.resources, name='resources'),
    path('index', views.index, name='home'),
    path('signupUser', views.signupUser, name='signupUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('game1', views.game1, name='game1'),
    path('game2', views.game2, name='game2'),
]