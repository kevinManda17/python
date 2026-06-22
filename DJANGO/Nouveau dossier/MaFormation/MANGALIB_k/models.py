from django.db import models

app_name="MANGALIB_k"

class Author(models.Model):
    name =models.CharField(max_length=64, unique=True, verbose_name="Nom")
     
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= "Auteur"
        verbose_name_plural="Auteurs"

class Book(models.Model):
    title= models.CharField(max_length=32, unique= True,verbose_name="Titre")
    quantity=models.IntegerField(default=1, verbose_name="Quantite")
    author=models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Auteur")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= "livre"
        verbose_name_plural="Livres"    

