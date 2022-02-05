from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    sub = models.CharField(primary_key=True, max_length=50)
    user_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> sub:
        return self.sub


class Paint(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    sub = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str(id):
        return str(id)


class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    comment = models.TextField()
    sub = models.ForeignKey(User, on_delete=models.CASCADE)
    paint_id = models.ForeignKey(Paint, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str(id):
        return str(id)
