from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class ContactInfo(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)
    postal_code = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_contact")
    
    def __str__(self):
        return f"{self.first_name}: {self.address}"