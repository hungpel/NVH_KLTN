from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from app.forms import AddConnectForm
from app.models import ConnectTicket
from libs import BaseViewMixin


class ConnectTicketCreateView(LoginRequiredMixin, BaseViewMixin, CreateView):
    model = ConnectTicket
    template_name = "pages/send_request.html"
    form_class = AddConnectForm

    def get_success_url(self) -> str:
        return reverse_lazy("connects-list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Bạn đã gửi connect thành công!!!")
        return super().form_valid(form)
