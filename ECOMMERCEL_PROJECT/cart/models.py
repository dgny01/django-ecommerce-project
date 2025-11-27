from django.db import models
from users.models import UserProfile
from products.models import Product
from decimal import Decimal

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
    def get_total_price(self):
        return self.quantity * self.product.price
    
class Order(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default="Pending")

    def __str__(self):
        return f"order {self.id} by {self.user.user.username}"
