from django.shortcuts import render, redirect
from .models import Products, Categories

# Create your views here.
def index(request):
    latest_products = Products.objects.all().order_by("-date")[:10]
    categories = Categories.objects.all()
    return render(request, "shop/index.html", {
        "latest_products": latest_products,
        "categories": categories,
    })

def search(request):
    category = ""
    querry = ""
    querry = request.GET["search"]
    if request.GET["category"]:
        category = Categories.objects.get(category=request.GET["category"])
    if category:
        results = Products.objects.filter(category=category, title__icontains=querry)
    else:
        results = Products.objects.filter(title__icontains=querry)
    if results is None:
        message = "No results returned"
    categories = Categories.objects.all()
    return render(request, "shop/index.html", {
        "latest_products": results,
        "categories": categories
    })