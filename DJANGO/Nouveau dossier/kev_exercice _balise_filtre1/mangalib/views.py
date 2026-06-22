from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

import datetime 

def index(request):
    context = {"message":"Hello world !",
               "numberNews":15,
               "usersList":["kevin", "regulation ","electronique","circuit logique "],
               "usersList2":[],
               "publication": datetime.datetime.now(),
               "d1":datetime.datetime.now(),
               "d2":datetime.datetime.now(),
               "username":""}
    template = loader.get_template("mangalib/index.html")
    return HttpResponse (template.render(context,request))

