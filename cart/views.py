from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from . models import CartList
from . models import Items
from accounts.models import Customer
from core.models import Products


SHIPPING_CHARGE = 40

@login_required(login_url='/accounts/login')
def index(request):
    cart_items = None
    cart = None
    try:
        customer = Customer.objects.get(user = request.user)
        cart = CartList.objects.get(user = customer)
        cart_items = Items.objects.filter(cart = cart)

        sub_total = 0

        for item in cart_items:
            sub_total += item.product.price * item.quantity
        
        total = sub_total + SHIPPING_CHARGE

    except:
        pass

    context = {
        'cart_items' : cart_items,
        'sub_total' : sub_total,
        'total' : total,
        'shipping_charge' : SHIPPING_CHARGE
    }

    return render(request,'cart.html',context)

@login_required(login_url='/accounts/login')
def add_to_cart(request,product_id):
    product = Products.objects.get(id = product_id)
    customer = Customer.objects.get(user = request.user)
    try:
        cart = CartList.objects.get(user = customer)
    except CartList.DoesNotExist:
        cart = CartList.objects.create(user = customer)
        cart.save()
    
    try:
        cart_item = Items.objects.get(product = product,cart = cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Items.DoesNotExist:
        cart_item = Items.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart:cart_index')

def add_count(request,product_id):
    product = Products.objects.get(id = product_id)
    customer = Customer.objects.get(user = request.user)
    cart = CartList.objects.get(user=customer)
    cart_item = Items.objects.get(product = product,cart = cart)
    quantity = cart_item.quantity
    if quantity < product.stock:
        cart_item.quantity += 1
        quantity = cart_item.quantity
        cart_item.save()
        response = JsonResponse({
            'quantity':quantity,
            'price' : product.price
        })
    else:
        response = JsonResponse({'quantity':'error'})
    return response

def reduce_count(request,product_id):
    product = Products.objects.get(id = product_id)
    customer = Customer.objects.get(user = request.user)
    cart = CartList.objects.get(user = customer)
    cart_item = Items.objects.get(product = product,cart = cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return JsonResponse({
            'quantity' : cart_item.quantity,
            'price': product.price,
        })
    else:
        cart_item.delete()
        return JsonResponse({'quantity' : 'empty'})
    

def delete_item(request,product_id):
    product = Products.objects.get(id=product_id)
    customer = Customer.objects.get(user=request.user)
    cart = CartList.objects.get(user=customer)
    cart_item = Items.objects.get(product = product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_index')
     