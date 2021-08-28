from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("", views.cart, name="cart"),
    path("add/<int:id>", views.add, name="add"),
    path("remove/<int:id>", views.remove, name="remove"),
]