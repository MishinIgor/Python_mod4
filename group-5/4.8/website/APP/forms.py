from django import forms 
from .models import Person
class StudentForm(forms.Form): 
    firstname = forms.CharField(label="Enter first name",max_length=50) 
    lastname  = forms.CharField(label="Enter last name", max_length = 100)

class MyForm(forms.Form):
    query = forms.CharField(label='Search')

class MyPostForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Ваш email')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']
