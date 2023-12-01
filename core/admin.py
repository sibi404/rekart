from django.contrib import admin
from . models import PlasticWaste,Category
from . models import Products
from . models import ProductCategory


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

class PlasticWasteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


admin.site.register(PlasticWaste,PlasticWasteAdmin)
admin.site.register(Category)
admin.site.register(Products,ProductAdmin)
admin.site.register(ProductCategory)