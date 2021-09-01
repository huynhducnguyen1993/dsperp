
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from .models import *
from .forms import *

from django.http.request import QueryDict

# Create your views here.


class Task_(View):
    def get(sefl, request):
        tasks = Task.objects.all().order_by('-id')
        form = TaskForm()
        context = {'tasks': tasks, 'form': form}
        return render(request, 'tasks/list.html', context)

    def post(self, request):
        form = TaskForm()

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('list')

        context = {'form': form, }
        return render(request, 'tasks/list.html', context)


def completeTask(request):
    id = request.GET.get('id')
    t = Task.objects.get(pk=id)
    qr =QueryDict('',mutable=True)
    ts = Task.objects.all()
    qr.update({
		'complete':True,
	})
    form = TaskForm_complete(qr,instance=t)
    if form.is_valid():
        form.save()
    context = {
        'tasks':ts,
    }
    return redirect("list")


def uncompleteTask(request):
	id = request.GET.get('id')
	t = Task.objects.get(pk=id)
	qr =QueryDict('',mutable=True)
	qr.update({
		'complete':False,
	})
	form = TaskForm_uncomplete(qr,instance=t)
	if form.is_valid():
		form.save()
	return redirect("list")
	

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('list')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
