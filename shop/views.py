from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "shop/index.html")
    else:
        return redirect("users:login")