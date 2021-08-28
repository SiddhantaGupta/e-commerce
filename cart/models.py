from django.db import models
from shop.models import Products
from users.models import User

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="desire")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shopper")