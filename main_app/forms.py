from django.forms import Form, CharField



class SearchForm(Form):


    city = CharField(label='city')  