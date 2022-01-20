from django.contrib import admin
from .models import User, Paint, Point
# Register your models here.

admin.site.register(User)
admin.site.register(Paint)
admin.site.register(Point)
