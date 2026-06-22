from django.shortcuts import *
from django.shortcuts import render , get_object_or_404
from .models import * 
from store.models import *
from .cart import Cart 
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages 


def cart_summary(request):
    cart = Cart(request)
    cart_products =cart.get_prods
    quantities= cart.get_quants
    totals=cart.cart_total()
    data = {
        "cart_products":cart_products ,
        "quantities":quantities,
        "totals":totals,
    }
    return render(request , 'cart_summary.html', data)

def cart_add(request):
    # get the cart 
    cart = Cart(request)
    # test for post 
    if request.POST.get('action') == "post":
        # get stuff 
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # lookup product in DB
        product= get_object_or_404(Product , id= product_id)
        # save to session 
        cart.add(product = product, quantity= product_qty )

        # get Cart Quantity
        cart_quantity = cart.__len__()

        # return response 
        # response = JsonResponse({'product Name': product.name })
        response = JsonResponse({'qty': cart_quantity })
        messages.success(request , ("Product Was Added Successfully To Your Cart !"))
        return response 



def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action') =='post':
        product_id = int(request.POST.get('product_id'))
        # call delete function in cart 
        cart.delete( product = product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request , ("Product Was Deleted SuccessFully From Your Cart !"))
        return response 

def cart_update(request):
    cart =Cart(request)
        # test for post 
    if request.POST.get('action') == "post":
        # get stuff 
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id , quantity=product_qty )
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ('Product Was Updated SuccessFully To Your Cart !'))
        return response 
        # return redirect('cart_summary')