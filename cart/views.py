from django.shortcuts import render, redirect
from .models import Cart
from shop.models import Products

# Create your views here.
def cart(request):
    wishlist = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart.html", {
        "wishlist": wishlist
    })

def add(request, id):
    product = Products.objects.get(pk=id)
    wish = Cart(product=product, user=request.user)
    wish.save()
    return redirect("shop:product", id=id)

def remove(request, id):
    product = Products.objects.get(pk=id)
    Cart.objects.get(product=product, user=request.user).delete()
    return redirect("shop:product", id=id)
