from django.db import models
from django import forms

# Create your models here.
class List(models.Model):
    subject=models.CharField(max_length=30, unique=True)
    item=models.CharField(max_length=100)
    complete=forms.BooleanField(required=False)

    def __str__(self):
        return self.subject