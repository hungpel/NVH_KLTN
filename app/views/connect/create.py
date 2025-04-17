from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import ConnectCreateForm
from app.models import Subject
from libs import BaseViewMixin


class ConnectCreateView(LoginRequiredMixin, BaseViewMixin, CreateView):
    template_name = "pages/add_request.html"
    form_class = ConnectCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy("connect-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Tạo mới 1 yêu cầu thành công!!!")
        return super().form_valid(form)
