from django import forms 
from .models import Meep  , Profile 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


#Profile Extras Form 
class ProfilePicForm(forms.ModelForm):
    profile_image= forms.ImageField(label='Profile Picture ')
    
    profile_bio= forms.CharField(label="Profile Bio " , widget=forms.widgets.Textarea(attrs={ 'class':'form-control',"placeholder": "Enter Your Bio  " , "class":"form-control" } ))
    homepage_link = forms.CharField(label ="", widget=forms.TextInput( attrs={'class':'form-control', 'placeholder':'Web site Link ' ,}))
    facebook_link = forms.CharField(label ="", widget=forms.TextInput( attrs={'class':'form-control', 'placeholder':'Facebook Link ' ,}))
    instagram_link =forms.CharField(label ="", widget=forms.TextInput( attrs={'class':'form-control', 'placeholder':'Instagram Link ' ,}))
    linkedin_link= forms.CharField(label ="", widget=forms.TextInput( attrs={'class':'form-control', 'placeholder':'LinkedIn Link',}))

    class Meta: 
        model = Profile 
        fields = ('profile_image', 'profile_bio' , 'homepage_link', 'facebook_link', 'instagram_link' ,'linkedin_link',  )
    

class MeepForm(forms.ModelForm):
    body = forms.CharField(required= True ,  widget = forms.widgets.Textarea(attrs={"placeholder": "Enter Your Post " , "class":"form-control" }) ,  label ="")

    class Meta: 
        model = Meep 
        exclude = ('user','likes',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget = forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Email address'})) 
    first_name = forms.CharField(label='' ,max_length=100 ,  widget = forms.TextInput(attrs={"class":"form-control", "placeholder":"First name "})) 
    last_name = forms.CharField(label='' ,max_length=100 ,  widget = forms.TextInput(attrs={"class":"form-control" , "placeholder":"Last name "})) 

    class Meta : 
        model = User 
        fields = ('username' ,'first_name', 'last_name' , 'email', 'password1' , 'password2' )
    
    
    def __init__(self , *args , **kwargs ):
        super(SignUpForm , self).__init__(*args , **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['username'].widget.attrs['placeholder'] ='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text= " "

        self.fields['password1'].widget.attrs['class'] ='form-control'
        self.fields['password1'].widget.attrs['placeholder'] = "password"
        self.fields['password1'].label=''
        self.fields['password1'].help_text= " "

        self.fields['password2'].widget.attrs['class']  ='form-control'
        self.fields['password2'].widget.attrs['placeholder'] ='password again  '
        self.fields['password2'].label=''
        self.fields['password2'].help_text= " "
