from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDos

def index(request):
    # database'de kaydettiğimiz todo ları çekebilmemiz için "object" isimli bir method var. Onu kullanacaz:
    todo_list = ToDos.objects.all() # models.py de oluşturduğumuz ToDos class'ındaki tüm objeleri getir dyoruz
    return render(request, "todo_application/index.html", {"todo_list":todo_list})
    # database deki tüm verileri aldık. Şimdi de index.html e gidip bunu görselleştirmemiz lazım...

def about(request):
    return render(request, "todo_application/about.html")

def create(request):
    return render(request, "todo_application/create.html")

"""
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is index page!")

# return edip çıktı göstermesini sağlamak için 'from django.http import HttpResponse' şeklinde HttpResponse'u import ememiz gerekyor.
# Ayrıca todo_project in settings.py dosyasının INSTALLED_APPS kısmında 'todo_app' şeklide uygulamamızı tanıtırız...

def about(request):
    return HttpResponse("This is about page!")

"""