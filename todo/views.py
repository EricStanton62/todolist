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

    return render(request,'home.html', {'all_tasks': all_tasks})  

def removal(request, pk):
    all_tasks=Todo.objects.all()
    tasks=get_object_or_404(Todo,pk=pk)

    if request.method =="GET":
        
        tasks.delete()
        return redirect('task_list')

    return render(request, 'home.html', {'all_tasks': all_tasks})   

def edit(request, pk):
    all_tasks=Todo.objects.all()
    current_task=Todo.objects.get(id=pk)

    if request.method=="GET":
        return render(request,'edit.html', {'current_task': current_task}, {'all_tasks': all_tasks})
    else: 
        frog=request.POST['edit']
        current_task.task=frog
        if current_task.task not in all_tasks:
            current_task.save()
        
    return redirect('task_list')

def completed(request, pk):
    all_tasks=Todo.objects.all()

