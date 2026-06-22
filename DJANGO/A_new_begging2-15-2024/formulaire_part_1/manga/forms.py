from django import forms 
from .models import Author , Book


class BookForm(forms.ModelForm):
    author= forms.ModelChoiceField(queryset=Author.objects.all(), label="Auteur")
  
    class Meta():
        model = Book
        fields = ["title","author", "quantity"]
        labels = {"title":"Titre","author":"Auteur" ,"quantity":"Quantite"}

        