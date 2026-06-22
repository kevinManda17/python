from django.shortcuts import render, get_object_or_404 ,  redirect
from django.http import HttpResponse 
from django.template  import loader 
from .models import Book , Author
from .forms import BookForm
from django.contrib.auth.decorators import login_required , permission_required , user_passes_test

"""
    django Guardian 
    Rules 
"""
app_name="manga"

def is_outsiders(user):
    return user.groups.filter(name="outsiders")

def index(request):
    data = {'message':'hello Kevin Manda',"books":Book.objects.all()}
    return render(request ,"manga/index.html" ,data)

# @permission_required('manga.view_book', raise_exception=True)
@user_passes_test(is_outsiders)
def show(request , book_id):
    data= {"book":get_object_or_404(Book, pk = book_id)}
    return render(request, 'manga/show.html', data)
    

@permission_required('manga.add_book', raise_exception=True)
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

@permission_required('manga.change_book', raise_exception=True)
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

@permission_required('manga.delete_book', raise_exception=True) 
def remove(request, book_id):
    book= Book.objects.get( pk= book_id)
    book.delete()
    return redirect("manga:index")
