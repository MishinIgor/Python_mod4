from django import forms 
from .models import *

class ProductPostForm(forms.ModelForm):
    class Meta:
        model = Product
        #fileds = "__all__"
        fields = ['title','brand','price']