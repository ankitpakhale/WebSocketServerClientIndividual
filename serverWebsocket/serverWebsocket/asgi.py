"""
ASGI config for serverWebsocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""


# old code start

# import os
# from django.core.asgi import get_asgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serverWebsocket.settings')
# application = get_asgi_application()

# old code end


# new code start
# import os
# from django.core.asgi import get_asgi_application
# from serverWebsocket.websocket import websocket_applciation

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serverWebsocket.settings')
# django_application = get_asgi_application()

# async def application(scope, receive, send):
#     if scope['type'] == 'http':
#         # Let Django handle HTTP requests
#         await django_application(scope, receive, send)
#     elif scope['type'] == 'websocket':
#         # We'll handle Websocket connections here
#         await websocket_applciation(scope, receive, send)
#     else:
#         raise NotImplementedError(f"Unknown scope type {scope['type']}")
# new code end


# new code 2 start
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from  .routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serverWebsocket.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    # Just HTTP for now. (We can add other protocols later.)
})
# new code 2 end