from django import forms
from .models import Cartoon


class CartoonForm(forms.ModelForm):
    class Meta:
        model=Cartoon
        fields=['name','desc','year','img']
