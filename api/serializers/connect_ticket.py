from rest_framework import serializers

from app.models import ConnectTicket


class ConnectTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectTicket
        fields = ["accepted"]

    def save(self, **kwargs):
        return super().save(**kwargs)
