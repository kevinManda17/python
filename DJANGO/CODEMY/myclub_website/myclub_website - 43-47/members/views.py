from django.shortcuts import render ,redirect
from django.contrib.auth import login , logout , authenticate 
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def register_user(request):
   
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password =form.cleaned_data["password1"]
            user = authenticate(username = username , password = password )
            login(request, user )
            messages.success(request , ("Registration SuccessFull !!"))
            return redirect("home")
    else :
        form = RegisterUserForm()
    data = {
            "form":form,
    }
    return render(request, "authenticate/register_user.html", data )

def logout_user(request):
    logout(request)
    messages.success(request , ("You Were Logged Out! "))
    return redirect("home")




def login_user(request):
    data = {

    }
        
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username , password = password )
        
        if user is not None :
            login(request , user )
            return redirect("home")
        else : 
            messages.success(request , ("There Was An Error Logging, Try Again "))
            return redirect("login")
    
    
    else  :
        return render(request, "authenticate/login.html" , data )
   
    
