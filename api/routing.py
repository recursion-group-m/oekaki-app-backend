from django.urls import path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<uuid:room_id>', ChatConsumer.as_asgi()),
]
