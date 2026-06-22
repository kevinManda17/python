from django.shortcuts import render , get_object_or_404, redirect
from .models import Book, Author
from django.contrib.auth.decorators import login_required ,permission_required


"""

quelques methodes apropos des permissions 
    user.has_perm()
        .all()
        .add() , add(<perm1> , ...)
        .remove(<perm1>, ...)
        .remove(<perm1> , ...)
        .clear()
        .set([])

"""


def index(request):
    data= {"books":Book.objects.all(),}
    return render(request, "MANGALIB_k/index.html", data)

@permission_required('MANGALIB_k.delete_book', raise_exception=True)
def show(request , book_id):
    data= {"book":get_object_or_404(Book, pk=book_id),}
    return  render(request, "MANGALIB_k/show.html", data )

def add(request):
    author= Author.objects.get(name="Akira toriyama")
    book= Book.objects.create(title="Dragon ball z", quantity=1345 , author = author )
    return redirect(request,"MANGALIB_k/index",)

def edit(request):
    book= Book.objects.get(title="dragon ball")
    book.title= "Dragon ball super"
    book.save()
    return redirect(request, "MANGALIB_k/index") 

def remove(request, book_id):
    book=Book.objects.get(pk=book_id)
    book.delete()
    return redirect(request,"MANGALIB_K/index")
