from rest_framework import serializers
from .models import User, Paint, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = '__all__'


class ReadCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


class WriteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
