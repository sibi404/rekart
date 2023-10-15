from django.shortcuts import render
from django.http import HttpResponse

from . models import PlasticWaste,Category
from . models import Products
from . models import ProductCategory

# Create your views here.

def index(request):
    
    request.session['sample'] = ['sample data']
    request.session['sample'].insert(0,'zero data')
    print(vars(request.session))

    plastics = PlasticWaste.objects.all()
    products= Products.objects.all()
    categories = Category.objects.values_list('short_name',flat=True)[:4]
    product_categories = ProductCategory.objects.all()

    

    context = {'plastics':plastics,'products':products,'categories':categories,'product_cats':product_categories}

    return render(request,'index.html',context)
