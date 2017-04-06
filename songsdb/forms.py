from django import forms

class AddForm(forms.Form):
    song_name = forms.CharField(label='Song name', max_length=50)
    document_link = forms.CharField(label='Document link', max_length=200)
    year = forms.IntegerField(label='Published year', max_value=2100, min_value=1800)
    author = forms.CharField(label='Author', max_length=50)
    publisher = forms.CharField(label='Publisher', max_length=50)
    song_type = forms.CharField(label='Song type', max_length=50)

class SearchForm(forms.Form):
    search_bar = forms.CharField(label='Enter keyword', max_length=200)
    search_field = forms.ChoiceField(label='Search for', choices=(('name', 'Name'),
     ('year', 'Year'),
     ('author', 'Author'),
     ('Publisher', 'Publisher'),
     ('type', 'Type')))
