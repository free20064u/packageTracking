from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signIn/', views.signInView, name="signIn"),
    path('signOut/', views.signOutView, name="signOut"),
]