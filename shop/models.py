from django.db import models

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

    def __str__(self):
        return f"{self.title}"

class Images(models.Model):
    image = models.ImageField(upload_to='product')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_image")