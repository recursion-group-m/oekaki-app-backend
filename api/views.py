from rest_framework import viewsets
from .models import Comment, User, Paint
from .serializers import (
    ReadCommentSerializer,
    WriteCommentSerializer,
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


class ReadCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ReadCommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["paint_id"]
    ordering = ['created_at']


class WriteCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = WriteCommentSerializer
