from django import forms
from .models import Todo


class NewTask(forms.ModelForm):
    task=forms.CharField(label="next item",max_length=50, required=True,)
    is_complete=forms.BooleanField(required=True, initial=False)

    class Meta:
        model=Todo
        fields=['task', 'is_complete']
        
