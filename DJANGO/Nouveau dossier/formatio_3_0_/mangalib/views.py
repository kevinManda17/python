from django.shortcuts import render, get_object_or_404, redirect
from .models import Book , Author
from django.contrib.auth.decorators import login_required , permission_required


def index(request):
    data = {"books":[]}
    return render(request,'mangalib', data )

def show(request, book_id):
    data={"book":get_object_or_404(Book, pk=book_id),}
    return render(request,'mangalib/show.html', data)