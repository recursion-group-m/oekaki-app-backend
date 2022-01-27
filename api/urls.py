from rest_framework import routers
from .views import (
    MessageViewSet,
    RoomViewSet,
    UserViewSet,
    PaintViewSet,
    PointViewSet
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paints', PaintViewSet, basename='Paints')
router.register(r'points', PointViewSet, basename='Points')
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)
urlpatterns = router.urls
