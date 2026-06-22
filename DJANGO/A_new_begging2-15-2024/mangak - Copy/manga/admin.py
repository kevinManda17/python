from django.contrib import admin
from .models import Author , Book 




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields= ["author", 'title', 'quantity']
    fieldsets=[
        ('Information du manga',{'fields':['author', 'title']}),
        ('Information du magasin',{"fields":['quantity']})
    ]

    list_display=('title', 'author' , 'quantity')
    list_filter=["author"]
    search_fields=['title']
    # list_per_page=6

# admin.site.register(Author, AuthorAdmin)  a utiliser sans decorateurs 
# admin.site.register(Book, BookAdmin)


