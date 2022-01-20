import django_filters
from .models import User, Paint


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = []


class PaintFilter(django_filters.FilterSet):
    class Meta:
        model = Paint
        fields = []
