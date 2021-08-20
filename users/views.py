from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegistrationForm
from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.is_valid()
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confirmation_password = form.cleaned_data["confirmation_password"]

        if password != confirmation_password:
            return render(request, "users/register.html", {
                "message": "Passwards did not match",
                "form": form
            })
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
            except IntegrityError:
                return render(request, "users/register.html", {
                    "message": "Email already exists",
                    "form": form
                })
            return redirect("users:login")
    else:
        return render(request, "users/register.html", {
            "form": RegistrationForm
        })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("shop:index")
        else:
            return render(request, "users/login.html", {
                "message": "email or password is invalid"
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("users:login")

def profile(request):
    return render(request, "users/profile.html")