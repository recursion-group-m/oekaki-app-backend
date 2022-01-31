from rest_framework import viewsets
# from .models import Message, Room, User, Paint, Point
# from .serializers import (
#     MessageSerializer,
#     RoomSerializer,
#     UserSerializer,
#     PaintSerializer,
#     PointSerializer
# )
# from .filters import UserFilter, PaintFilter
from .models import Message
from .serializers import MessageSerializer
# Create your views here.


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_class = UserFilter


# class PaintViewSet(viewsets.ModelViewSet):
#     queryset = Paint.objects.all()
#     serializer_class = PaintSerializer
#     filter_class = PaintFilter


# class PointViewSet(viewsets.ModelViewSet):
#     queryset = Point.objects.all()
#     serializer_class = PointSerializer


# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.prefetch_related('messages')
#     serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
