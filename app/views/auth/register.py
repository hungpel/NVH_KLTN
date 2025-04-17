from django.contrib.auth import login
from django.shortcuts import redirect, render

from app.forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "pages/register.html", {"form": form})
