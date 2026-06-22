# stuff about request 
from django.shortcuts import *
from django.shortcuts import render , redirect 

# stuff about email 
from django.core.mail import * 
from django.core.mail import send_mail , send_mass_mail 



def index(request):
    return render(request , "base.html", {
        
    })
    


def contact(request):
    
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
    
        # send an email 
        
        send_mail(
            message_name, # subject 
            message, # message 
            message_email, # from email 
            ['kevmulambomm@gmail.com'], # To email 
        )
    
    
        return render(request , "contact.html", {"name":message_name , "email":message_email , "message":message ,
        
        })
    
    else :  
        return render(request , "contact.html", {
        
        })