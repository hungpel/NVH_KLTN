from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class SignIn(FormView):
    template_name = "pages/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
