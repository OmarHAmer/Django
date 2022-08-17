from sys import maxsize
from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':5}))