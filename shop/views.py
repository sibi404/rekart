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



def product_view(request,product_id):
    product = Products.objects.get(id = product_id)
    print(product.name)

    context = {
        'product' : product
    }
    return render(request,'detail.html',context)

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
            return redirect('shop:product_details',product_id = product.id)
    else:
        form = ProductsForm(instance=product)
    return render(request,'new.html',{'form':form})


def delete_product(request,product_id):
    product = Products.objects.get(id = product_id)
    product.delete()
    return redirect('shop:shop')
