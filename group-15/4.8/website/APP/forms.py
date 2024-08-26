from django import forms

class MyForm(forms.Form):
    query = forms.CharField(label='Search')


        