from django.urls import re_path

from .consumers import SnapConsumer

websocket_urlpatterns = [
    re_path(r'ws/sensor/data/', SnapConsumer.as_asgi()),
]