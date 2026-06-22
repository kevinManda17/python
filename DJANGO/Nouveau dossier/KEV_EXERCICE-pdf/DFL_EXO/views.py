from django.shortcuts import render
from django.http import HttpResponse
def myHome():
    return HttpResponse("Bonjour a tous ")
