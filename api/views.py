from rest_framework import viewsets
from .models import Comment, User, Paint
from .serializers import (
    CommentSerializer,
    UserSerializer,
    PaintSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaintViewSet(viewsets.ModelViewSet):
    queryset = Paint.objects.all()
    serializer_class = PaintSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["paint_id"]
    ordering = ['created_at']
