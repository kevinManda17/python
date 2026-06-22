from django.shortcuts import render , get_object_or_404 , redirect
from .models import Book, Author 

def index(request):
    data= {"books":Book.objects.all(),}
    
    return render(request, "MANGALIB_k/index.html", data)


def show(request , book_id):
    data= {"book":get_object_or_404(Book,pk=book_id)}
    return  render(request, "MANGALIB_k/show.html", data )

def add(request):
    author= Author.objects.get(name="Akira toriyama")
    book= Book.objects.create(title="Dragon ball Z", quantity=1024, author= author  )

    return  redirect(request , "MANGALIB_k:index")