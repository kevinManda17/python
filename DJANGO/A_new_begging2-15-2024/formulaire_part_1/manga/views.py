from django.shortcuts import render, get_object_or_404 ,  redirect 
from django.http import HttpResponse 
from django.template  import loader 
from .models import Book , Author
from .forms import BookForm

# app_name="manga"

def index(request):
    data = {'message':'hello Kevin Manda',"books":Book.objects.all()}
    return render(request ,"manga/index.html" ,data)

def show(request , book_id):
    data= {"book":get_object_or_404(Book, pk = book_id)}
    return render(request, 'manga/show.html', data)


def add(request):
    if request.method == "POST":
        form  = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manga:index')
    else :
        form= BookForm()
    data ={"form": form }
    return render(request, 'manga/manga_forms.html', data)

def edit(request, book_id):
    book = Book.objects.get( pk = book_id)
    if request.method == "POST":
        form  = BookForm(request.POST, instance= Book)
        if form.is_valid():
            form.save()
    else :
        form=BookForm(instance= Book)
    data= {"form": form}
    return render(request, 'manga/edit-books.html', data)

    
def remove(request, book_id):
    book= Book.objects.get( pk= book_id)
    book.delete()
    return redirect("manga:index")
