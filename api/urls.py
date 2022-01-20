from rest_framework import routers
from .views import UserViewSet, PaintViewSet, PointViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paints', PaintViewSet, basename='Paints')
router.register(r'points', PointViewSet, basename='Points')
urlpatterns = router.urls
