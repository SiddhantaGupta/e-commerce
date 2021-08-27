from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegistrationForm, ContactForm
from .models import User, ContactInfo

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

def contactInfo(request, id):
    addresses = ContactInfo.objects.filter(user=request.user)
    return render(request, "users/contactInfo.html", {
        "addresses": addresses
    })

def addContact(request, id):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.is_valid()
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        address = form.cleaned_data["address"]
        phone_number = form.cleaned_data["phone_number"]
        postal_code = form.cleaned_data["postal_code"]
        new_contact = ContactInfo.objects.create(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, postal_code=postal_code, user=request.user)
        new_contact.save()
        return redirect("users:contactInfo", id=id)

    return render(request, "users/addContact.html", {
        "form": ContactForm
    })

def deleteContact(request, contactId):
    ContactInfo.objects.get(pk=contactId).delete()
    return redirect("users:contactInfo", id=request.user.id)