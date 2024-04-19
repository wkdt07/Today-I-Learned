from django.contrib import admin

# Register your models here.
from .models import Comment,Board

admin.site.register(Comment)
admin.site.register(Board)