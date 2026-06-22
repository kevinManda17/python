from django.shortcuts import render , redirect
from .models import *
from .models import Product, Order, Customer, Category 
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .forms import SignUpForm

def  category(request, cat):
    cat = cat.replace('-', " ")
    category = Category
    products =Product
    try:
        category= Category.objects.get(name = cat )
        products = Product.objects.filter(category = category )
        data = {
            "category":category,
            "products":products,
        }
        return render(request , 'category.html', {'category':category , 'products':products } )
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
            messages.success(request , ("Registration Successfully! Welcome !"))
            return redirect('home')
        else :
            messages.success(request , ("There Was An Problems, We don't Know  Try Again Please"))
            return redirect('register')
    return render(request , 'register.html' , {'form':form,})
