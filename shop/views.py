from django.shortcuts import render
from django.shortcuts import redirect
from itertools import chain
from django.contrib.auth.models import User

from core.models import Category
from core.models import ProductCategory
from core.models import Products
from core.models import PlasticWaste

from . forms import ProductsForm
from . forms import PlasticWasteForm



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



def product_view(request,slug):
    product = Products.objects.get(slug = slug)

    context = {
        'product' : product,
        'item' : 'product'
    }
    return render(request,'product_detail.html',context)

def plastic_view(request,slug):
    plastic = PlasticWaste.objects.get(slug = slug)
    context = {
        'plastic' : plastic,
        'item' : 'plastic'
    }
    return render(request,'plastic_details.html',context)

def add_item(request):
    type = request.GET.get('type',None)

    if request.method == 'POST':
        if type == 'product':
            form = ProductsForm(request.POST,request.FILES)
        else:
            form = PlasticWasteForm(request.POST,request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            obj =  form.save(commit=False)
            obj.seller = user
            obj.save() 
        return redirect('/')
    else:
        if type == 'product':
            form = ProductsForm()
        else:
            form = PlasticWasteForm()

    context = {'form':form,'type' : type}

    return render(request,'new.html',context)

def update_product(request,product_id):
    product = Products.objects.get(id = product_id)
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES,instance=product)
        if form.is_valid:
            form.save()
            return redirect('shop:product_details',slug = product.slug)
    else:
        form = ProductsForm(instance=product)
    return render(request,'new.html',{'form':form,'type' : 'product','update':True})


def update_plastic(request,plastic_id):
    plastic = PlasticWaste.objects.get(id = plastic_id)
    if request.method == 'POST':
        form = PlasticWasteForm(request.POST,request.FILES,instance=plastic)
        if form.is_valid:
            form.save()
            return redirect('shop:plastic_details',slug = plastic.slug)
    else:
        form = PlasticWasteForm(instance=plastic)
    return render(request,'new.html',{'form':form,'type' : 'plastic','update' : True})


def delete_product(request,product_id):
    product = Products.objects.get(id = product_id)
    product.delete()
    return redirect('shop:shop')

def delete_plastic(request,plastic_id):
    plastic = PlasticWaste.objects.get(id = plastic_id)
    plastic.delete()
    return redirect('shop:shop')
