from rest_framework import viewsets
from .models import User, Paint, Point
from .serializers import UserSerializer, PaintSerializer, PointSerializer
from .filters import UserFilter, PaintFilter
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter


class PaintViewSet(viewsets.ModelViewSet):
    queryset = Paint.objects.all()
    serializer_class = PaintSerializer
    filter_class = PaintFilter


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
