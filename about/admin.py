from django.contrib import admin

# Register your models here.

from .models import About_Post, history_post

admin.site.register(About_Post)

admin.site.register(history_post)