from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDos
from .forms import ListForm


def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = ToDos.objects.all()
            return render(request, "todo_application/index.html", {"todo_list":todo_list})

    else:
        todo_list = ToDos.objects.all()
        return render(request, "todo_application/index.html", {"todo_list":todo_list})

    

def about(request):
    return render(request, "todo_application/about.html")



def create(request):

    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = ToDos.objects.all()
            return render(request, "todo_application/create.html", {"todo_list":todo_list})

    else:
        todo_list = ToDos.objects.all()
        return render(request, "todo_application/create.html", {"todo_list":todo_list})


def delete(request, ToDos_id):
    todo = ToDos.objects.get(pk = ToDos_id)
    todo.delete()
    return redirect("index")


def yes_finish(request, ToDos_id):
    todo = ToDos.objects.get(pk=ToDos_id)
    todo.finished = False # Şu an true olan buton, butona basınca False olsun
    todo.save()
    return redirect("index")


def no_finish(request, ToDos_id):
    todo = ToDos.objects.get(pk=ToDos_id)
    todo.finished = True # Şu an False olan buton, butona basınca True olsun
    todo.save()
    return redirect("index")


def update(request, ToDos_id):   # Yeni bir ToDo oluşturuyo gibi form gönderimi yapacaz. "create" fonksiyonu gibi...
    if request.method == "POST":
        todo_list = ToDos.objects.get(pk=ToDos_id)
        form = ListForm(request.POST or None, instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        todo_list = ToDos.objects.all()
        return render(request, "todo_application/update.html",{"todo_list":todo_list})
