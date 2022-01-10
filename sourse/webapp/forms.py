from django import forms
from django.forms import widgets
class BookForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, label='Текст', widget=widgets.Textarea(attrs={'rows':6, 'cols':50}))
    count = forms.IntegerField(min_value=0)
    price = forms.DecimalField(min_value=0, decimal_places=2)