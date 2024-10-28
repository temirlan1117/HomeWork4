from django.contrib import admin

import posts
from .models import Post, Tag,category,Comment

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title','content','rate', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

admin.site.register(Tag)
admin.site.register(category)
admin.site.register(Comment)

