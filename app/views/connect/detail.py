from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import Connect
from libs import BaseViewMixin


class ConnectDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Connect
    template_name = "pages/send_request.html"
