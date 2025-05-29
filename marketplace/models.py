from django.db import models
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal
from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=(('farmer', 'Farmer'), ('buyer', 'Buyer')))

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Model for Farmer Profile
class FarmerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    farm_name = models.CharField(
        max_length=200
    )
    location = models.CharField(
        max_length=200
    )
    contact_number = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.farm_name

# Model for Crop
class Crop(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE
    )
    crop_name = models.CharField(
        max_length=100,
        default="Unknown Crop"
    )
    quantity = models.IntegerField(
        default=0
    )
    price_per_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )
    harvest_date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} ({self.farmer.farm_name})"
# Model for Buyer Profile
class BuyerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=15
    )
    address = models.TextField()
    company_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    contact_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username


# market/models.py
from django.db import models

from django.db import models

class CropPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.crop_name



# contact form model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# Model for Product
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE , related_name='farmer_products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    posted_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name    
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # <-- Add this
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username}"


