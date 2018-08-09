from django import forms
from .models import TodoList


class NewTask(forms.Form):
    items=forms.CharField(label="next item",max_length=50, required=True,)
    
    class Meta:
        model=TodoList
        fields=['items']
