from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import List

def home(request):
    todo=List.objects.all()
    return render(request,'home.html', {'todo': todo})
# Create your views here.

def task(request):
    subject=get_object_or_404(List, pk=pk)
    return render(request,'task.html',{'subject': subject})
    
