from django.shortcuts import render
from django.http import HttpResponse

from . models import PlasticWaste,Category
from . models import Products
from . models import ProductCategory

# Create your views here.

def index(request):
    plastics = PlasticWaste.objects.all()[:4]
    products= Products.objects.all()[:4]
    categories = Category.objects.values_list('short_name',flat=True)[:4]
    product_categories = ProductCategory.objects.all()

    context = {'plastics':plastics,'products':products,'categories':categories,'product_cats':product_categories}

    return render(request,'index.html',context)
