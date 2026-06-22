from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template ,Context
from .models import Task

def home(request , name):
    return HttpResponse("Bonjour a tous "+ name)

def task_listing(request):
    data = Task.objects.all().order_by('due_date')
    template = Template("""
        {% for elem in data %}
                {{elem}} <br>
        {% endfor %}
""")
    print(str(template))
    context = Context({'data':data})
    print(str(template.render(context)))
    return HttpResponse(template.render(context))

