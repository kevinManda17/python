from django import forms 

class SomeForm(forms.Form):

    username= forms.CharField(label="Nom d'utilisateur", max_length=25)
    password= forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    bio= forms.CharField(label="biographie", widget=forms.Textarea)

    # la selection multiple

    publicate= forms.CharField(label="publier", widget=forms.CheckboxInput)
    languages= [('c', 'langage C'), ("php", "langage php")]
    language= forms.MultipleChoiceField(label="langages connus" ,widget=forms.CheckboxSelectMultiple , choices= languages)


    # radio 
    colors=[('1', 'Rouge'), ('2','Bleu'),('3',"vert")]
    color= forms.ChoiceField(label="couleur preferee",choices = colors, widget=forms.RadioSelect)

    # le select
    countries = [('fr', 'France'),('jp', 'japon'),('kr', "coree du sud")]
    contry=forms.ChoiceField(choices=countries , label= "pays ")