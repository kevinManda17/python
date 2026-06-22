from django.shortcuts import render , get_object_or_404, redirect
from .models import Book, Author
from .forms import SomeForm 

def index(request):
    if request.method == 'POST':
        form=SomeForm(request.POST)

        if form.is_valid():
            return redirect("mangalib_k:index")
    else :
        form= SomeForm()
    data={"form":form}
    return render(request, "MANGALIB_k/index.html", data)


def show(request , book_id):
    data= {
        "book":get_object_or_404(Book,pk=book_id),
    }
    return  render(request, "MANGALIB_k/show.html", data )

def add(request):
    author= Author.objects.get(name="Akira Toriyama")
    book= Book.objects.create(title="Dragon ball z", quantity=1345 , author = author )
    return redirect("MANGALIB_k:index", request)

def edit(request):
    book= Book.objects.get(title="dragon ball")
    book.title= "Dragon ball super"
    book.save()

    return redirect("MANGALIB_k:index")