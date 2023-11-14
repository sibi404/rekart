from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer')
    is_seller = models.BooleanField()

    def __str__(self):
        return self.user.username
