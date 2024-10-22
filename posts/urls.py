from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('http_response', views.http_response, ),
    path('html_response', views.html_response, ),
    path('posts/', views.post_list , ),
    path('posts/<int:post_id>/', views.post_detail_view , ),
    ]
