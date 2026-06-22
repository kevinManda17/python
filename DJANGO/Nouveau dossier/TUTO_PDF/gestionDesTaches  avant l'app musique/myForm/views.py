from django.shortcuts import render
from .models import Utilisateur ,Email, ListeDiffusion


def contact(request):
    data = {}   
  
    return render(request,"contact.html", data)

# On crée 2 utilisateurs

user1 = Utilisateur(nom='user1')
user2 = Utilisateur(nom='user2')

# On crée les mails associés

email1 = Email(mail='user1@baba.fr', user=user1)
email2 = Email(mail='user2@bibi.fr', user=user2)

# On crée 4 listes de diffusion

liste1 = ListeDiffusion(listeName='liste1')
liste2 = ListeDiffusion(listeName='liste2')
liste3 = ListeDiffusion(listeName='liste3')
liste4 = ListeDiffusion(listeName='liste4')

# on sauvegarde tout le monde

user1.save()
user2.save()
email1.save()
email2.save()
liste1.save()
liste2.save()
liste3.save()
liste4.save()

# on ajoute les emails à des listes

liste1.email.add(email1)
liste1.email.add(email2)
liste2.email.add(email1)
liste3.email.add(email1)
liste3.email.add(email2)
liste4.email.add(email2)

# Pour obtenir toutes les listes auxquelles l'email1 est abonné :
email1.listes.all()
# Et celles auxquelles l'email2 est abonné :
email2.listes.all()

def emial_detail(request , pk ):
    email=Email.objects.get(pk = pk)
    user =email.user
    listes_abonnees = email.listes.all()
    template = "email_detail.html"
    context = {'user': user , 'email':email , "listes":listes_abonnees}

    return render(request , template ,context)