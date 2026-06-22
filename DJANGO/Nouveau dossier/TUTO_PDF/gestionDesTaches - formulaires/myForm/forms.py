from django.forms.fields import DateField, ChoiceField
from .forms import forms , MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms import SelectDateWidget



BIRTH_YEAR_CHOICES = ('1999', '2000', '2001')

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