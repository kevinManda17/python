from django.shortcuts import render , redirect 
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages  

# app_name="accounts"

def login_user(request):
    if request.method == "POST":
        username= request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username = username, password = password )
        if user is not None :
            login(request, user )
            return redirect("manga:index")
        else :
            messages.info(request , "Identifiant ou mot de passe incorrect. ")
    form= AuthenticationForm()
    data ={"form_connection": form }
    return render(request , 'accounts/login.html', data)
def logout_user(request):
    logout(request)
    return redirect("manga:index")

def register_user(request):
    if request.method =="POST":
        form= UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("manga:index")
        
    else :
        form = UserCreationForm()
    data= {"form_register": form }
    return render(request , "accounts/register.html", data )



