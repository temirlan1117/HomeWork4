from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('http_response', views.http_response, ),
    path('html_response', views.html_response, ),
    ]
