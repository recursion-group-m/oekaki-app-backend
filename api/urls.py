from rest_framework import routers
from .views import (
    UserViewSet,
    PaintViewSet,
    ReadCommentViewSet,
    WriteCommentViewSet
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paints', PaintViewSet, basename='paints')
router.register(r'read-comments', ReadCommentViewSet, basename='read-comments')
router.register(
    r'write-comments',
    WriteCommentViewSet,
    basename='write-comments'
)
urlpatterns = router.urls
