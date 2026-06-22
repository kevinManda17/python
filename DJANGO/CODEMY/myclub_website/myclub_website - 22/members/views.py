from django.shortcuts import render ,redirect
from django.contrib.auth import login , logout , authenticate 
from django.contrib import messages 



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
   
    
