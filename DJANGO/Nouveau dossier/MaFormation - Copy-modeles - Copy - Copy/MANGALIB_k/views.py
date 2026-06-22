from django.shortcuts import render , get_object_or_404
from .models import Book

def index(request):
    data= {"books":Book.objects.all(),
        
           }
    
    return render(request, "MANGALIB_k/index.html", data)


def show(request , book_id):
    data= {
        "book":get_object_or_404(Book,pk=book_id),
    }
    return  render(request, "MANGALIB_k/show.html", data )