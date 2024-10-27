from django.contrib import admin
from django.urls import path, include
from posts.views import (
http_response,
html_response,
post_list,
post_detail_view,
post_create_view,
comment_create_view
)
from users.views import register_view, login_view, logout_view



urlpatterns = [

    path('http_response', http_response, ),
    path('html_response', html_response, ),
    path('posts/', post_list , ),
    path('posts/<int:post_id>/', post_detail_view , ),
    path('post_create/', post_create_view , ),
    path('posts_comment/', comment_create_view,),
    path("register/", register_view),
    path("login/", login_view),
    path("logout/", logout_view),

    path('', post_list),
    ]
