# # your_project_name/asgi.py
# import os

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from . import routing # Import file routing.py của project

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter(
#         routing.websocket_urlpatterns
#     ),
# })