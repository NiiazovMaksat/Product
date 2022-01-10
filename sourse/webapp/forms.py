from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, label='Текст',
                                  widget=widgets.Textarea(attrs={'rows': 6, 'cols': 50}))
    category = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label="Категория", initial=STATUS_CHOICES[0][1])
    count = forms.IntegerField(min_value=0)
    price = forms.DecimalField(min_value=0, decimal_places=2)
