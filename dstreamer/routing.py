from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumer import StreamConsumer
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import re_path

websocket_urlpatterns = [
    path('ws/stream/', StreamConsumer.as_asgi(timeout=60)),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r'ws/(?P<mode>\w+)/(?P<stream_id>\w+)/$', StreamConsumer.as_asgi()),
            ]
        )
    ),
})