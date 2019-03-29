from django import forms

class QueryForm(forms.Form):
	source = forms.CharField(label='',widget=forms.TextInput(attrs={'id': 'myInput', 'placeholder':'Water Data'}))

