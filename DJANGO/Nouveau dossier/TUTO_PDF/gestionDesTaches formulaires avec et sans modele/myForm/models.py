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
