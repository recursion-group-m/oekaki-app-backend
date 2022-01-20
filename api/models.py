from django.db import models

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
