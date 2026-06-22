from django.shortcuts import *
from django.shortcuts import render , get_object_or_404
from .models import * 
from store.models import *
from .cart import Cart 
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    cart =Cart(request)
    cart_products = cart.get_prods 
    data = { 
        "cart_products":cart_products,
    }
    return render(request , 'cart_summary.html', data)

def cart_add(request):
    # get the cart 
    cart = Cart(request)
    # test for post 
    if request.POST.get('action') == "post":
        # get stuff 
        product_id = int(request.POST.get('product_id'))
        # lookup product in DB
        product= get_object_or_404(Product , id= product_id)
        # save to session 
        cart.add(product = product )


        # return response 
        response = JsonResponse({'product Name': product.name })
        return response 



def cart_delete(request):
    data = {}
    return render(request , 'cart_delete.html', data)

def cart_update(request):
    data = {}
    return render(request , 'cart_update.html', data)