from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template ,Context
from .models import Task

def home(request , name):
    return HttpResponse("Bonjour a tous "+ name)

def task_listing(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request , template_name="lesTaches/list.html", context={"tasks":tasks})


def task_listing2(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request , template_name="lesTaches/list2.html", context={"tasks":tasks})

