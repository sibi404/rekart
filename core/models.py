from django.db import models



class Category(models.Model):
      name = models.CharField(max_length=50)
      short_name = models.CharField(max_length=10)
      description = models.TextField()


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


class Products(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField()
      stock = models.PositiveIntegerField()
      price = models.DecimalField(max_digits=10,decimal_places=2)