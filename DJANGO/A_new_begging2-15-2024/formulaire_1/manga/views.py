from django.shortcuts import render, get_object_or_404 ,  redirect 
from django.http import HttpResponse 
from django.template  import loader 
from .models import Book , Author

from .forms import SomeForm

# app_name="manga"

def index(request):
    data = {'message':'hello Kevin Manda',
            "books":Book.objects.all(),
        # "books":Book.objects.all().order_by("-title"),
        # "books":Book.objects.all().filter(title='Dragon ball')
        
        }
    return render(request ,"manga/index.html" ,data)

def show(request , book_id):
    data= {"book":get_object_or_404(Book, pk = book_id)}

    return render(request, 'manga/show.html', data)


def add(request):
    author= Author.objects.get(name="Akira toriyama")
    book= Book.objects.create(title="Dragon ball Z", quantity=131, author= author)

    # sans le gestionnaire 
    # book= Book(title="Dragon ball", quantity=131, author= author)
    # book.save()
    return  redirect("manga:index")

def edit(request):
    book= Book.objects.get(title="Dragon ball Z")
    book.title ="Dragon ball super"
    book.save()
    return redirect("manga:index")

def remove(request):
    book= Book.objects.filter(title__startswith="Dragon ball")
    book.delete()
    return redirect("manga:index")

def forms(request):
    if request.method == "POST":
        form= SomeForm(request.POST)

        if form.is_valid():
            return redirect("manga:forms")
    else :
        form = SomeForm()
    data ={"form": form}
    return render(request,"manga/forms.html", data)

    # return render(request , "manga/forms.html", data)