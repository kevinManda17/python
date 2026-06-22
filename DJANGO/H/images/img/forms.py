from django import forms 
from .models import Image , Project 

class ProjetForm(forms.ModelForm):
    class Meta : 
        model = Project 
        fields= (
            'name',
            "slug",
            "description"
        )
class Imageform(forms.ModelForm):
    image= forms.ImageField(label="image" , widget=forms.ClearableFileInput(attrs={"multiple":True }))

    class Meta: 
         model = Image 
         fields=('image',)


# class ProjectForm(ProjectPartForm):
#     images= forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple":True}))

#     class Meta(ProjectPartForm.Meta) : 
#         fields = ProjectPartForm.Meta.fields + [ 'images',]