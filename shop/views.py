from django.shortcuts import render
from itertools import chain

from core.models import Category
from core.models import ProductCategory
from core.models import Products
from core.models import PlasticWaste


from . forms import EmployeeForm

def shop(request):
    plastic_category = Category.objects.values_list('short_name',flat=True)
    product_category = ProductCategory.objects.values_list('name',flat=True)
    categories = list(chain(plastic_category,product_category))


    category = request.GET.get('category',0)

    products = None
    plastic_waste = None

    
    if category:
        if category == 'P':
            products = Products.objects.all()
        elif category == 'W':
            plastic_waste = PlasticWaste.objects.all()
        else:
            products = Products.objects.filter(category__name=category)
            plastic_waste = PlasticWaste.objects.filter(category__short_name=category)

    else:
        products = Products.objects.all()
        plastic_waste = PlasticWaste.objects.all()

    context = {
        'categories':categories,
        'products':products,
        'plastic_waste':plastic_waste,
        'category_name':category
    }

    return render(request,'shop.html',context)



def product_view(request,product_id):
    product = Products.objects.get(id = product_id)
    print(product.name)

    context = {
        'product' : product
    }
    return render(request,'detail.html',context)

def add_item(request):

    form = EmployeeForm()

    return render(request,'new.html',{"form":form})
