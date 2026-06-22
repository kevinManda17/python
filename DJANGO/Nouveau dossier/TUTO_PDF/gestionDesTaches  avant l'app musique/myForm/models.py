from django.db import models
from django.contrib import admin

class Contact(models.Model):
    name = models.CharField(max_length= 200)
    firstname = models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    message= models.CharField(max_length=1000)


class Author(models.Model):
    name =models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    birth_date=models.CharField(max_length=200)


class User(models.Model):
    username = models.CharField(max_length=150)
    class Meta:
        db_table="user"

    def __str__(self):
        return self.username
    
class Task(models.Model):
    name =models.CharField(max_length=250)
    decription = models.TextField()
    creation_date= models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    utilisateur= models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    class Meta :
        db_table="task"

    def __str__(self):
        return self.name
    

class Utilisateur(models.Model):
    nom  = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    
    # def __str__(self):
    #     return "%s %s" % (self.prenom , self.nom)
    class Meta:
        db_table="utilisateur"

class Email(models.Model):
    mail= models.CharField(max_length=30)
    user=models.ForeignKey(Utilisateur , on_delete=models.CASCADE , null=True , related_name="emails")

    def __str__(self):
        return self.mail 
    class Meta:
        db_table= "email"

class ListeDiffusion(models.Model):
    listeName = models.CharField(max_length=30)
    email=models.ManyToManyField(Email, related_name='listes')


    def __str__(self):
        return self.listeName
    
    class Meta:
        db_table = "listeDiffision"