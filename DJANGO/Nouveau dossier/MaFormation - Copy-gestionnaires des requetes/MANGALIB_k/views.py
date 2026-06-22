from django.shortcuts import render , get_object_or_404, redirect
from .models import Book, Author

def index(request):
    data= {"books":Book.objects.all(),
        
           }
    
    return render(request, "MANGALIB_k/index.html", data)


def show(request , book_id):
    data= {
        "book":get_object_or_404(Book,pk=book_id),
    }
    return  render(request, "MANGALIB_k/show.html", data )

def add(request):
    author= Author.objects.get(name="Akira Toriyama")
    book= Book.objects.create(title="Dragon ball z", quantity=1345 , author = author )
    return redirect("MANGALIB_k:index")
