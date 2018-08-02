from django import forms
from .models import List

class Listform(form.ModelForm):
    message=forms.CharField(max_length=100)

    class Meta:
        model = List
        fields = ['subject', 'message']