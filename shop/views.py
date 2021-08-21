from django.shortcuts import render, redirect
from .models import Products, Categories, Images

# Create your views here.
def index(request):
    latest_products = Products.objects.all().order_by("-date")[:5]
    return render(request, "shop/index.html", {
        "latest_products": latest_products,
    })