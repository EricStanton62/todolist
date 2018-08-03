from django import forms
from .models import TodoList
from crispy_forms.helper import FormHelper

class Listform(form.Form):
    item=forms.CharField(label="next item",max_length=50, required=True,)
    def __init__(self):
