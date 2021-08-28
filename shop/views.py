from django.shortcuts import render, redirect
from .models import Products, Categories, Comments, Purchases
from users.models import ContactInfo
from cart.models import Cart

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

def product(request, id):
    product = Products.objects.get(pk=id)
    comments = Comments.objects.filter(product=product)
    in_cart = False
    if request.user.is_authenticated:
        wishlist = Cart.objects.filter(user=request.user)
        for wish in wishlist:
            if product.id == wish.product.id:
                in_cart = True

    return render(request, "shop/product.html", {
        "product": product,
        "comments": comments,
        "in_cart": in_cart,
    })

def comment(request, id):
    if request.method == "POST":
        product = Products.objects.get(pk=id)
        review = Comments(comment=request.POST["comment"], user=request.user, product=product)
        review.save()
        return redirect("shop:product", id=id)

def purchase(request, id):
    if request.method == "POST":
        quantity = int(request.POST["quantity"])
        address_id = request.POST["address"]
        address = ContactInfo.objects.get(pk=address_id)
        product = Products.objects.get(pk=id)
        purchase = Purchases(product=product, user=request.user, quantity=quantity, deliver_to=address)
        purchase.save()
        product.quantity = product.quantity - quantity
        product.save()
        total_amount = product.price * quantity
        return render(request, "shop/success.html", {
            "amount": total_amount,
        })

    product = Products.objects.get(pk=id)
    addresses = ContactInfo.objects.filter(user=request.user)
    return render(request, "shop/purchase.html", {
        "product": product,
        "addresses": addresses,
    })