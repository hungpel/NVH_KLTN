from django import template

from app.models import ConnectTicket

register = template.Library()


@register.filter(name="get_accepted_people")
def get_accepted_people(connect):
    return ConnectTicket.objects.filter(connect=connect, accepted=True).count()
