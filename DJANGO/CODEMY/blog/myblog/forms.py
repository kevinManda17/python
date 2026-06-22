from django import forms 
from .models import * 
from .models import Post , Category , Comment


# choices = [("coding", "coding" ),("sports","sports") ,("entertrianement", "entertrainement")]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices : 
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title','header_image','title_tag','author','category','body','snippets')

        widgets= {
            "title": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
            # 'hearder_image':forms.ImageField(),
            "title_tag": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
            "author": forms.TextInput(attrs={'class':'form-control' , 'value':'', 'id':'post_owner', 'type':'hidden', }),
            # "author": forms.Select(attrs={'class':'form-control' , 'placeholder':''}),
            "category": forms.Select(choices=choice_list ,attrs={'class':'form-control' , 'placeholder':''}),
            "body": forms.Textarea(attrs={'class':'form-control' , 'placeholder':''}),
            "snippets": forms.Textarea(attrs={'class':'form-control' , 'placeholder':''}),
        }

class EditForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title','header_image','title_tag','body','snippets')

        widgets= {
            "title": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
            "title_tag": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
            "body": forms.Textarea(attrs={'class':'form-control' , 'placeholder':''}),
            "snippets": forms.Textarea(attrs={'class':'form-control' , 'placeholder':''}), 
        }

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ('name','body')

        widgets= {
            "name": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
            "body": forms.Textarea(attrs={'class':'form-control' , 'placeholder':''}),
        }