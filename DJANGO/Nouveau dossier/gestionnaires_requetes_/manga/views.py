from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author


def index(request):
    data ={"books":Book.objects.all()}
    template=loader.get_template('manga/index.html')
    return HttpResponse(template.render(data, request))

def show(request, book_id):
    data={'book':get_object_or_404(Book, pk=book_id)}
    return render(request, 'manga/show.html', data)

def add(request):
    author= Author.objects.get(name="Akira toriyama")
    book=Book.objects.create(title="Dragon ball Z", quantity=132, author= author)
    book.save()
    return  redirect('manga:index')

def edit(request):
    book= Book.objects.get(title="Dragon ball")
    book.title ="Dragon ball super"
    book.save()
    return redirect('manga:index')

def remove(request):
    book=Book.objects.filter(title__startswith="Dragon ball")
    book.delete()
    return redirect("manga:index")