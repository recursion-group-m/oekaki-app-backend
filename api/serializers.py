from rest_framework import serializers
from .models import Room, User, Paint, Point


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = '__all__'
        depth = 1


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'
        depth = 1


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
