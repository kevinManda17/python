from django.shortcuts import render, redirect
from  django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages

def login_user(request):

    if request.method == 'POST' :
        username=request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request , username= username , password= password)
        if user is not None :
            login(request , user)
            return redirect("MANGALIB_k:index") 
        else :
            messages.info(request , "Identifiant ou mot de passe incorrect !")

    form= AuthenticationForm()
    return  render( request, "account/login.html", {"form":form})

def logout_user(request):
    # pass 
    logout(request)
    return redirect("MANGALIB_k:index") 

def register_user(request):
    if request.method =="POST" :
        form= UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("MANGALIB_k:index")
    else :
        form= UserCreationForm()

    return render(request, "account/register.html", {"form":form})