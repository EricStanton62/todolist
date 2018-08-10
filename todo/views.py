from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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

def removal(request, pk):
    items=get_object_or_404(TodoList,pk=pk)

    if request.method =="POST":
        items.delete()

        return redirect('task')

    return render(request, 'removal.html', {'items': items})   
