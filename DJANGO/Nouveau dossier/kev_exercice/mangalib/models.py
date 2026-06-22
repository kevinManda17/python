from django.db import models

""" Une classe pour les models fait kevin """

class  Author(models.Model):
    name = models.CharField(max_length=64, unique= True )

class Book(models.Model):
    title= models.CharField(max_length=32, unique= True )
    quatity= models.IntegerField(default=1)
    author = models.ForeignKey(Author,on_delete =models.DO_NOTHING)
    