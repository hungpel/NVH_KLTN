from rest_framework import status, viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.response import Response

from api.serializers import LikeSerializer
from app.models import Like


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    authentication_classes = (
        CsrfExemptSessionAuthentication,
        BasicAuthentication,
    )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        headers = self.get_success_headers(serializer.data)
        if data:
            return Response(
                {"type": "like"},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        return Response(
            {"type": "unlike"}, status=status.HTTP_201_CREATED, headers=headers
        )
