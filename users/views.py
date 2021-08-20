from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.is_valid()
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confirmation_password = form.cleaned_data["confirmation_password"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]

        if password != confirmation_password:
            return render(request, "users/register.html", {
                "message": "Passwards did not match",
                "form": form
            })
        else:
            user = User(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect("login")
    else:
        return render(request, "users/register.html", {
            "form": RegistrationForm
        })

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return render(request, "")
        else:
            return render(request, "user/login.html", {
                "message": "email or password is invalid"
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")