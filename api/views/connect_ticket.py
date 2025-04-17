from rest_framework import mixins, viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)

from api.serializers import ConnectTicketSerializer
from app.models import ConnectTicket


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class ConnectTicketViewSet(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    serializer_class = ConnectTicketSerializer
    queryset = ConnectTicket.objects.all()

    authentication_classes = (
        CsrfExemptSessionAuthentication,
        BasicAuthentication,
    )

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
