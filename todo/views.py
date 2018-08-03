from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TodoList

   
# Create your views here.
def task(request):
    item=TodoList.objects.all()

    return render(request,'home.html', {'item': item})    
