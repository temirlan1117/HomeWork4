from django.contrib import admin
from webbrowser import register
from users.models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'age')
# Register your models here.
