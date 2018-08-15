from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import NewTask
from django import forms
   
# Create your views here.

def task(request):
    all_tasks=Todo.objects.all()
    if request.method=='POST':
        new_task=request.POST['task']
        if new_task is not "":
            new_task_temp = Todo.objects.create(task=new_task)
            return redirect('task_list')
    
        return redirect('task_list')
    

    return render(request,'home.html', {'all_tasks': all_tasks, })  

def removal(request, pk):
    all_tasks=Todo.objects.all()
    current_task=get_object_or_404(Todo,pk=pk)

    if request.method =="GET":
        
        current_task.delete()
        return redirect('task_list')

    return render(request, 'home.html', {'all_tasks': all_tasks})   

def edit(request, pk):
    all_tasks=Todo.objects.all()
    current_task=Todo.objects.get(id=pk)

    if request.method=="GET":
        return render(request,'edit.html', {'current_task': current_task}, {'all_tasks': all_tasks})
    else: 
        task_edit=request.POST['edit']
        current_task.task=task_edit
        current_task.save()
        
    return redirect('task_list')

def completed(request):
    all_tasks=Todo.objects.all()
    return render(request, 'completed.html', {'all_tasks': all_tasks})

def move_completed(request, pk):
    all_tasks=Todo.objects.all()
    current_task=Todo.objects.get(id=pk)

    if request.method=="GET":
        funtastic=request.GET.get('done')
        if not funtastic:
            if current_task.is_complete is False:
                current_task.is_complete=True
                current_task.save()
                return render(request, 'home.html', {'all_tasks': all_tasks, })
            else:
                current_task.is_complete=False
                current_task.save()
                return redirect('completed')
    return render(request,'completed.html', {'all_tasks': all_tasks, }) 

