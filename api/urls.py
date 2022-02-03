from rest_framework import routers
from .views import (
    UserViewSet,
    PaintViewSet,
    CommentViewSet
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paints', PaintViewSet, basename='paints')
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = router.urls
