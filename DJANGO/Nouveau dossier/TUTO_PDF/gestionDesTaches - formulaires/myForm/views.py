from django.shortcuts import render
from myForm.models import Contact , Author
from django import forms 
from django.forms import ModelForm , Textarea ,SelectDateWidget 
from django.forms.fields import DateField, ChoiceField ,MultipleChoiceField 
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

# autre contenu 
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages



class ContactForm(ModelForm):
    pass
    class Meta():   
        model= Contact
        fields= ('name', "firstname", "email", "message")
        widget = {
            'message':Textarea(attrs={'cols':60 , 'rows':10}),
        }

# un formulaire creer a la main  sans model 

class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email =forms.CharField(max_length=200)
    message=forms.CharField(max_length=1000)



BIRTH_YEAR_CHOICES = ('1999', '2000', '2001' , '2002' , '2003')

GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))

FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
('green', 'Green'),
('black', 'Black'))

class SimpleForm(forms.Form):
    birth_year = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    gender = ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
    favorite_colors = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

class CommentForm(forms.Form):
    name = forms.CharField(
    widget=forms.TextInput(attrs={'class':'special'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))

    # venant des modeles 
class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        widgets = {
        'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


def contact(request):
    contact_form = ContactForm()
    contact_form2 = ContactForm2()
    simple_form= SimpleForm()
    comment_form =CommentForm()
    list_forms ={'contact_form':contact_form ,
                 'contact_form2':contact_form2,
                 'simple_form':simple_form,
                "comment_form":comment_form,
    }     
  
    return render(request,"contact.html", list_forms)

# autre contenu 

class ContactForm(ModelForm):
    def __init__(self):
        super(ContactForm, self).__init__()
        self.fields['name'].label = "Nom "
        self.fields['firstname'].label = "Prenom"
        self.fields['email'].label = "mél"
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email','message')
        widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10}),
        }
        def contact(request):
            form = ContactForm()    # on instancie un formulaire

            if request.method == "POST":                #on teste si on est bien en validation de formulaire (POST)
                form = ContactForm(request.POST)        # Si oui on récupère les données postées
                if form.is_valid():                     # on vérifie la validité du formulaire
                    new_contact = form.save()           # on prépare un nouveau message
                    messages.success(request,'Nouveau contact '+new_contact.name+ '' +new_contact.email)
                    #return redirect(reverse('detail', args=[new_contact.pk] ))
                    context = {'pers': new_contact}
                    return render(request,'detail.html', context)
                context = {'form': form}                # Si méthode GET, on présente le formulaire
            return render(request,'contact.html', context)








def detail(request, cid):
    contact = Contact.objects.get(pk=cid)
    context = {'pers': contact}
    return render(request,'myForm/detail.html', context)

