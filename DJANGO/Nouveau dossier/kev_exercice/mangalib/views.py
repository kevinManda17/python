from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
# from django.template import loader
from .models import Book , Author 

"""
SELECT : all() , get()
ORDER BY: order_by()
LIMIT : [:N]
WHERE : filter(name_cols= "value")
            __gt , __lt , __gte, __lte, __ startswith 
INSERT INTO : create()
"""

 
def index(request):
    context = {"books": Book.objects.all(),
            #    "books":Book.objects.order_by("title"),
            #    "books": Book.objects.all()[:5],
            # "books":Book.objects.all().filter(title= "Naruto"),
            # "books": Book.objects.all().filter(title__startswith= "naruto" ),
            # "books":Book.objects.all().filter(quatity__gt= 200),
            # "books":Book.objects.all().filter(title= "Naruto"),
            # "books":Book.objects.all().filter(title= "Naruto")
               }
    
    return render(request,"mangalib/index.html",context)

def show(request , book_id):
    context= {"book":get_object_or_404(Book, pk= book_id) }
    return render(request, "mangalib/show.html",context)

def add(request):
    author=  Author.objects.get(name="Akira Toriyama ")
    book = Book.objects.create(title="Dragon ball Z", quatity=13 , author= author)
    book.save()
    return redirect("mangalib:index")
