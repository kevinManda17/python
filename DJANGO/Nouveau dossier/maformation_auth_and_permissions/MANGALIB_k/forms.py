from django import forms

class SomeForm(forms.Form):
        # username= forms.CharField(label="Nom d'utilisateur")
        # password=forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
        # bio=forms.CharField(label="Biographie", widget=forms.Textarea)

        # languages=[("C","Langage C"), ('PHP', "Langage PHP ")]
        # language= forms.MultipleChoiceField(label="Langage connu", widget=forms.CheckboxSelectMultiple, choices=languages)

        # colors=[('1','rouge'), ('2','Bleu',),('3', 'Vert')]
        # color=forms.ChoiceField(label="Couleur Dominante", choices=colors, widget=forms.RadioSelect)
        countries= [('fr', 'France'),('jp',"japon"),('kr', 'Coree du sud ')]
        country= forms.ChoiceField(label="Pays", choices=countries ,)