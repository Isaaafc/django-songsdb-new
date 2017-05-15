from django import forms
from .models import Author, Publisher, Type

class AddForm(forms.Form):
    song_name = forms.CharField(label='Song name', max_length=50)
    document_link = forms.CharField(label='Document link', max_length=200)
    year = forms.IntegerField(label='Published year', max_value=2100, min_value=1800)
    author = forms.CharField(label='Author', max_length=50, required=False)
    author_choice = forms.ModelChoiceField(label='Author', queryset=Author.objects.all(), required=False)
    publisher = forms.CharField(label='Publisher', max_length=50, required=False)
    publisher_choice = forms.ModelChoiceField(label='Publisher', queryset=Publisher.objects.all(), required=False)
    song_type = forms.CharField(label='Song type', max_length=50, required=False)
    type_choice=forms.ModelChoiceField(label='Song type', queryset=Type.objects.all(), required=False)

class SearchForm(forms.Form):
    search_bar = forms.CharField(label='Enter keyword', max_length=200)
    search_field = forms.ChoiceField(label='Search for', choices=(('name', 'Name'),
     ('year', 'Year'),
     ('author', 'Author'),
     ('Publisher', 'Publisher'),
     ('type', 'Type')))
