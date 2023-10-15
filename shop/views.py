from django.shortcuts import render
from itertools import chain

from core.models import Category
from core.models import ProductCategory
from core.models import Products
from core.models import PlasticWaste


def shop(request):
    plastic_category = Category.objects.values_list('short_name',flat=True)
    product_category = ProductCategory.objects.values_list('name',flat=True)
    categories = list(chain(plastic_category,product_category))
    
    context = {'categories':categories}

    category = request.GET.get('category',0)




    return render(request,'shop.html',context)

