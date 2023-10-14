from django.contrib import admin
from . models import PlasticWaste,Category
from . models import Products
from . models import ProductCategory


admin.site.register(PlasticWaste)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(ProductCategory)