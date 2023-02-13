from django.forms import Form, CharField
from django.forms import forms



class SearchForm(Form):


    city = CharField(label='city' 'country', max_length=100)  

