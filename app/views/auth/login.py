from typing import Any

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView


class LoginView(FormView):
    template_name = "pages/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")

    def post(
        self, request: HttpRequest, *args: str, **kwargs: Any
    ) -> HttpResponse:
        form = self.get_form()

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().form_invalid(form)
