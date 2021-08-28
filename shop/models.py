from django.db import models
from users.models import User, ContactInfo

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.category}"

class Products(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=164)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="products")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="reviews")

class Purchases(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name="purchased_item")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    quantity = models.IntegerField()
    deliver_to = models.ForeignKey(ContactInfo, on_delete=models.PROTECT, related_name="delivery_address")
    delivery_status = models.BooleanField(default=False)