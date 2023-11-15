from django.db import models
from accounts.models import Customer
from core.models import Products
# Create your models here.

class CartList(models.Model):
    user = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='cart')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart"


class Items(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
