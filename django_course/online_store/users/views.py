from django.shortcuts import render
from django.forms import modelform_factory
from django.shortcuts import redirect
from .models import User

# Create your views here.

RegisterForm = modelform_factory(User, exclude=[])


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/welcome")
    else:
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})