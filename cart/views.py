from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
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
            sub_total += item.product.price
        
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




def delete_item(request,product_id):
    product = Products.objects.get(id=product_id)
    customer = Customer.objects.get(user=request.user)
    cart = CartList.objects.get(user=customer)
    cart_item = Items.objects.get(product = product,cart=cart)
    cart_item.delete()
    return redirect('cart_index')
     