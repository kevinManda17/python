from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=64, unique=True, verbose_name='Nom')

class Book(models.Model):
    title=models.CharField(max_length=32, unique=True, verbose_name='Titre')
    quantity=models.IntegerField(default=1, verbose_name='quantite')
    author=models.ForeignKey(Author,on_delete=models.DO_NOTHING, verbose_name="Auteur")

     