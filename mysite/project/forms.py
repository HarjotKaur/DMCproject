from django import forms

class SearchForm(forms.Form):
    search = forms.IntegerField()
class FilterForm(forms.Form):
    department=forms.CharField(max_length=200)
