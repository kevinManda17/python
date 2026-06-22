from django.shortcuts import render, get_object_or_404 ,  redirect 
from django.http import HttpResponse 
from django.template  import loader 
from .models import Book , Author

# app_name="manga"

"""
 les methodes save() , delete()

select :    all(): *
            get("argument"): un seul enregistrement 
insert:     create()
where:      filter("argument")
            __gt , __lt , __gte , __lte , __startswith
order by   : order by("argument")
limit :[:N] premier enregistrement , N --> int 

pour ecrire du slq pur , on applique au gestionnaire la methode 
        telle RAW(
          SELECT * FROM table WHERE name= 'kevin' 
        )

"""

def index(request):
    data = {'message':'hello Kevin Manda',
            "books":Book.objects.all(),
        # "books":Book.objects.all().order_by("-title"),
        # "books":Book.objects.all().filter(title='Dragon ball')
        
        }


    # avec un loader 
    # template = loader.get_template('manga/index.html')
    # return HttpResponse(template.render(data , request))
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