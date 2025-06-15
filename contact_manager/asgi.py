import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import contacts.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contact_manager.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(contacts.routing.websocket_urlpatterns)
    ),
})

