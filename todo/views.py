from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TodoList
from .forms import NewTask
   
# Create your views here.
def task(request):
    items=TodoList.objects.all()

    if request.method=='POST':
        item=request.POST['task']

        task = TodoList.objects.create(
            item=item
        )
        return redirect('task')

    return render(request,'home.html', {'items': items})    
