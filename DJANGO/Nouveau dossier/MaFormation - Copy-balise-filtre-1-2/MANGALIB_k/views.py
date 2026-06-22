from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
import datetime

def index(request):
    data= {"message":"Hello Django's world here , i'm kevin Manda !",
           "numbernews": 1,
           'userlist':['ELECTRONIQUE','INFORMATIQUE','ROBOTIQUE','AUTOMATION'],
           'userlist2':[],
           'publication':datetime.datetime.now(),
           'd1':datetime.datetime.now(),
           'd2':datetime.datetime.now(),
           'username':'',
           'username2':None,
           "texte":"""je suis un grand 
           texte j'ai besoin d'etre tronquer 
           alors fais quelque pour que 
           ca arrive stp parce que je sens 
           que je suis trop long comme texte  """,
           'link':""" N'oubliez pas ceci http://lestechnologies.cd/index.html?toujoursAvec=Electronique&p=20 sur mangalib_k"""
           }
    template= loader.get_template("MANGALIB_k/index.html")

    return HttpResponse(template.render(data, request))