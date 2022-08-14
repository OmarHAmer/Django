from pyexpat import model
from django import forms
from .models import Apply

class ApplyForms(forms.ModelForm):
    class Meta :
        model = Apply
        fields = ['name','email','website','cover_letter']
