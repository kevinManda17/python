from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.template  import loader 
from .models import Book

def index(request):
    data = {'message':'hello Kevin Manda',
        "books":Book.objects.all()}

    # avec un loader 
    # template = loader.get_template('manga/index.html')
    # return HttpResponse(template.render(data , request))
    return render(request ,"manga/index.html" ,data)

def show(request , book_id):
    data= {"book":get_object_or_404(Book, pk = book_id)}

    return render(request, 'manga/show.html', data)
