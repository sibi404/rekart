from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
      name = models.CharField(max_length=50)
      short_name = models.CharField(max_length=10)
      description = models.TextField()

      def __str__(self):
            return self.name


class ProductCategory(models.Model):
      name = models.CharField(max_length=20)

      def __str__(self):
            return self.name

class PlasticWaste(models.Model):
    class UnitChoices(models.TextChoices):
            KILOGRAM = 'KG','Kilogram'
            METRIC_TON = 'MT','Metric Ton'
            POUNDS = 'lb','Pounds'

    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=2,choices=UnitChoices.choices,default='')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plastic_image',blank=True,null=True)
    seller = models.ForeignKey(User,related_name='plastic_waste',on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField(default="",null=True)

    def __str__(self):
          return self.name


class Products(models.Model):
      class CategoryChoice(models.TextChoices):
            FURNITURE = 'Furniture'
            HOME_ACCESSORIES = 'Home accessories'
            STATIONEY = 'Stationery'
            BAGS = 'Bags'

      name = models.CharField(max_length=100)
      description = models.TextField()
      stock = models.PositiveIntegerField()
      price = models.DecimalField(max_digits=10,decimal_places=2)
      image = models.ImageField(upload_to='product_image',blank=True,null=True)
      seller = models.ForeignKey(User,related_name='products',on_delete=models.CASCADE,null=True,blank=True)
      category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True)
      slug = models.SlugField(default="",null=True)

      def __str__(self):
            return self.name