from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("product/<int:id>", views.product, name="product"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("purchase/<int:id>", views.purchase, name="purchase"),
    path("purchases", views.purchases, name="purchases"),
]