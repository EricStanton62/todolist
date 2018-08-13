from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import NewTask
   
# Create your views here.

def task(request):
    items=TodoList.objects.all()
    if request.method=='POST':
        item=request.POST['task']
        try:
            task = TodoList.objects.create(item=item)
        except:
            "do nothing"
        return redirect('task')

    return render(request,'home.html', {'items': items})  

def removal(request, pk):
    items=TodoList.objects.all()
    tasks=get_object_or_404(TodoList,pk=pk)

    if request.method =="GET":
        
        tasks.delete()
        return redirect('task')

    return render(request, 'home.html', {'items': items})   

def edit(request, pk):
    items=TodoList.objects.all()
    task=TodoList.objects.get(id=pk)

    if request.method=="GET":
        return render(request,'edit.html', {'task': task}, {'items': items})
    else: 
        frog=request.POST['edit']
        task.item=frog
        if task.item not in items:
            task.save()
        
    return redirect('task')
