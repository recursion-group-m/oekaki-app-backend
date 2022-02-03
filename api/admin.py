from django.contrib import admin
from .models import Comment, User, Paint
# Register your models here.

admin.site.register(User)
admin.site.register(Paint)
admin.site.register(Comment)
