from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.coverpage, name='coverpage'),
    path('about', views.about, name='about'),
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
    path('gad7Test', views.gad7Test, name='gad7Test'),
    path('phq9Test', views.phq9Test, name='phq9Test'),
    path('k10Test', views.k10Test, name='k10Test'),
    path('submit_k10', views.submit_k10, name='submit_k10'),
    path('submit_gad7', views.submit_gad7, name='submit_gad7'),
    path('submit_phq9', views.submit_phq9, name='submit_phq9'),
]