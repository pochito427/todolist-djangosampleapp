from django.shortcuts import render, redirect
from . models import Task
from . forms import TaskForm, AddWorkedTimeForm
from django.contrib import messages
from zeep import Client
# Create your views here.
def home(request):
    if(request.method == "POST"):
        form = TaskForm(request.POST or None)
        if(form.is_valid()):
            form.save()
            all_tasks = Task.objects.all
            messages.success(request, ('La tarea ha sido creada!!!'))
            return render(request, "home.html", {'all_tasks': all_tasks})
    else:
        all_tasks = Task.objects.all
        return render(request, "home.html", {'all_tasks': all_tasks})

def edit_worked_time(request, task_id):
    task = None
    task = Task.objects.get(pk=task_id)
    return render(request, "edit_worked_time.html", {'task': task})


def add_worked_time(request):
    if(request.method == "POST"):
        form = AddWorkedTimeForm(request.POST or None)
        if(form.is_valid()):
            task_id = request.POST.get('task_id')
            task = Task.objects.get(pk=task_id)
            time_to_add_string = request.POST.get('worked_time')
            old_worked_time = int(task.worked_time)
            time_to_add = int(time_to_add_string)
            client = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
            updated_worked_time = client.service.Add(old_worked_time, time_to_add)
            task.worked_time = float(updated_worked_time)
            task.save()
            all_tasks = Task.objects.all
            messages.success(request, ('El tiempo trabajado en la tarea ha sido agregado!!!'))
            return render(request, "home.html", {'all_tasks': all_tasks}) 
    else:
        all_tasks = Task.objects.all
        return render(request, "home.html", {'all_tasks': all_tasks})