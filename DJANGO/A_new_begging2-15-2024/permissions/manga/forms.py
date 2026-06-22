from django import forms 
from .models import Author , Book


class BookForm(forms.ModelForm):
    author= forms.ModelChoiceField(queryset=Author.objects.all(), label="Auteur")
  
    class Meta():
        model = Book
        fields = ["title","author", "quantity"]
        labels = {"title":"Titre","quantity":"Quantite"}

    def clean_quantity(self):
        quantity= self.cleaned_data['quantity']
        if quantity < 1 or quantity > 100 :
            raise forms.ValidationError("La quantite du livre devra etre comprise entre 1 et 100 ")
        return quantity
    
    def clean(self):
        title = self.cleaned_data.get('title')
        quantity = self.cleaned_data.get('quantity')
        
        if title and quantity :
            if title.startswith("Dragon ball") and quantity < 10 :
                raise forms.ValidationError("La quantite des livres dragon ball doit etre superieur a 10 ")

        return self.cleaned_data
    