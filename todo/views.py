from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import List

def home(request):
    return render(request,'home.html', {'todo': todo})
# Create your views here.
