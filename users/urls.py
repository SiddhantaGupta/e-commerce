from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path("contactInfo/<int:id>", views.contactInfo, name="contactInfo"),
    path("<int:id>/addContact", views.addContact, name="addContact"),
    path("<int:contactId>/deleteContact", views.deleteContact, name="deleteContact")
]