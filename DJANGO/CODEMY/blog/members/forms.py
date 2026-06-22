from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
from django.contrib.auth.models import User 
from django import forms 
from myblog.models import Profile 

class ProfilePageForm(forms.ModelForm):
    class Meta: 
        model= Profile 
        fields=('bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url','pinterest_url', )
        widgets= {
                "bio": forms.Textarea(attrs={'class':'form-control' , 'placeholder':''}),
                # 'hearder_image':forms.ImageField(),
                # "profile_pic": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
                "website_url": forms.TextInput(attrs={'class':'form-control', }),
                "facebook_url": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
                "twitter_url": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
                "instagram_url": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
                "pinterest_url": forms.TextInput(attrs={'class':'form-control' , 'placeholder':''}),
            }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='' ,widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email' }))
    first_name= forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name ',}))
    last_name= forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name',}))


    class Meta : 
        model= User 
        fields= ('username', 'first_name','last_name', 'email','password1', 'password2')


    def __init__(self , *args , **kwargs ):
        super(SignUpForm , self).__init__(*args , **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['username'].widget.attrs['placeholder'] ='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text= ''


        self.fields['password1'].widget.attrs['class'] ='form-control'
        self.fields['password1'].widget.attrs['placeholder'] = "password"
        self.fields['password1'].label=''
        self.fields['password1'].help_text= ''


        self.fields['password2'].widget.attrs['class']  ='form-control'
        self.fields['password2'].widget.attrs['placeholder'] ='Password Confirmation'
        self.fields['password2'].label=''
        self.fields['password2'].help_text= ''



class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email' }))
    first_name= forms.CharField( max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name ',}))
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name',}))
    username= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name',}))
    last_login= forms.CharField( max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name',}))
    is_superuser= forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check', 'placeholder':'Last Name',}))
    is_staff= forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check', 'placeholder':'Last Name',}))
    is_active= forms.CharField( max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check', 'placeholder':'Last Name',}))
    date_joined =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date Joined',}))
    

    class Meta : 
        model= User 
        fields= ('username', 'first_name','last_name', 'email',  'password' , 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined',)

class PasswordChangingForm(PasswordChangeForm):
    old_password= forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password ', 'type':
    'password', }))
    new_password1= forms.CharField(label='', max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'new Password','type':
    'password',}))
    new_password2= forms.CharField(label='', max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password Again ','type':
    'password',}))

    class Meta : 
        model= User 
        fields= ('username', 'first_name','last_name', 'email','password1', 'password2')