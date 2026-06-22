from django.shortcuts import render , redirect
from .models import *
from .models import Product, Order, Customer, Category ,Profile 
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .forms import SignUpForm , UpdateUserForm ,ChangePasswordForm , UserInfoForm 
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.db.models import Q
import json 
from cart.cart import Cart 



def  search(request):
    # determine if they filled out the page 
    if request.method == "POST":
        searched = request.POST['searched']
        # query the product database model 
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains= searched ))
        # test for null 
        if  not searched:
            messages.success(request, ("There's Not Products For Your Searched. Sorry !!! ")) 
        return render(request, 'search.html', {'searched': searched})
    else:
        return render(request , 'search.html', {})





def update_info(request):
    if request.user.is_authenticated:
        # get current user 
        current_user = Profile.objects.get( user__id = request.user.id)
        # get current user's shipping info 
        shipping_user = ShippingAddress.objects.get(user__id =request.user.id )
        # get original user form
        form = UserInfoForm(request.POST or None , instance = current_user)
        shipping_form =ShippingForm(request.POST or None , instance=shipping_user )

        if form.is_valid() or shipping_form.is_valid():
            # save form 
            form.save()
            # save shipping form 
            shipping_form.save()
        
            messages.success(request , ('Your Informations Have Been Updated'))
            return redirect('home')
        return render(request , 'update_info.html', {'form':form,'shipping_form':shipping_form})
    else :
        messages.success(request, ('You Must Be Logged To View This Page'))
        return redirect('home')
    return render(request , 'update_info.html', {})


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user 
        # did they fill out the form 
        if request.method == "POST":
            form = ChangePasswordForm(current_user , request.POST)
            # is form valid 
            if form.is_valid():
                form.save()
                messages.success(request , ('Your Password Has Been Updated , Please Login Again ! '))
                # login(request , current_user )
                return redirect('login')
            else :
                for error in list(form.errors.values()):
                    messages.error(request , error )
                return redirect('update-password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request , 'update_password.html', {'form':form,})
    else :
        messages.success(request , ('You Must Be Logged To View This Page '))
        return redirect('home')
    return render(request, 'update_password.html' , {'form':form,})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get( id = request.user.id)
        user_form = UpdateUserForm(request.POST or None , instance = current_user)
        if user_form.is_valid():
            user_form.save()
            login(request , current_user )
            messages.success(request , ('User Has Been Updated'))
            return redirect('home')
        return render(request , 'update_user.html', {"user_form":user_form})
    else :
        messages.success(request, ('You Must Be Logged To View This Page'))
        return redirect('home')



def category_summary(request):
    categories = Category.objects.all()
    data ={
        'categories':categories,
    }
    return render(request , 'category_summary.html', data )


def  category(request, cat):
    cat = cat.replace('-', ' ')
    category = ''
    products =''
    # grab the category from the url 
    try:
        # look up the category 
        category= Category.objects.get(name = cat )
        products = Product.objects.filter(category = category )
        return render(request , 'category.html', { 'products':products, 'category':category , } )
    except:
        messages.success(request, ("The Category Doesn't exists "))
        redirect('home')
    
    return render(request , 'category.html' , {
        "category":category,
        "products":products,
    })


def product(request , pk):
    product = Product.objects.get(pk = pk )
    data = {
        "product":product,
    }
    return render(request, 'product.html', data )


# home view
def home(request):
    products= Product.objects.all()
    data={"products":products,}
    return render(request, "home.html" , data )
# about us view 
def about(request):
    data={}
    return render(request, "about.html", data )
# create login and logout functions views 

def login_user(request):       # login 
    if request.method  == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(request , username= username , password = password)
        if user is not None :
            login(request , user )
            # DO something cart stuff 
            current_user = Profile.objects.get(user__id= request.user.id )
            # get the save cart form  database 
            saved_cart = current_user.old_cart

            # convert database string  to oython dictionnary
            if saved_cart :
                # convert to dictionnary using json
                converted_cart =json.loads(saved_cart)
                # Add the loaded cart dictionnary to your session 
                # get the cart 
                cart =Cart(request)              # Lookup the cart and the item 
                cart=Cart(request)
                for key , value in  converted_cart.items():
                    cart.db_add(product= key , quantity= value )

            messages.success(request , ("You Have Been Logged In "))
            return redirect('home')
        else :
            messages.success(request , ("There Was An Error ! Please Try Again..."))
            return redirect('login')
    else :
        return render(request , 'login.html', {})

def logout_user(request):      #logout
    logout(request)
    messages.success(request, ("You Have Been Logged Out ... Thanks For Stopping By ..."))
    return redirect('home')


# register user view 
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(username= username , password= password)
            login(request , user)
            messages.success(request , ("Registration Successfully! Welcome ..."))
            return redirect('update-info')
        else :
            messages.success(request , ("There Was An Problems, We Don't Know ! Try Again Please"))
            return redirect('register')
    return render(request , 'register.html' , {'form':form,})
