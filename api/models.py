from django.db import models
from model_utils.models import UUIDModel
from django.utils import timezone
# Create your models here.


class User(models.Model):
    sub = models.CharField(primary_key=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> sub:
        return self.sub


class Paint(models.Model):
    sub = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=50)
    width = models.IntegerField()
    tool = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str(number):
        return str(self.number)


class Point(models.Model):
    sub = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.ForeignKey(Paint, on_delete=models.CASCADE)
    point = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str(point):
        return str(self.point)


class Room(UUIDModel, models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False
)


class Message(UUIDModel, models.Model):
    room = models.ForeignKey(
        Room,
        related_name='messages',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, editable=False
)
