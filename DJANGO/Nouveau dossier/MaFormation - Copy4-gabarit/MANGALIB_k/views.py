from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

def index(request):
    data= {"message":"Hello Django's world here , i'm kevin Manda !"
           }
    template= loader.get_template("MANGALIB_k/index.html")

    return HttpResponse(template.render(data, request))