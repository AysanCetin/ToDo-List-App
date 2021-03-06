from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"), # -2- views.index ---> todo_app in views dosyasında index isimli fonksiyon oluşturalım..
    path('about/', views.about, name = "about"), # -3- views.about ---> todo_app in views dosyasında about isimli fonksiyon oluşturalım..
    path('create/', views.create, name = "create"),
    path('delete/<ToDos_id>', views.delete, name = "delete"), # id ye özel silme ---> 'delete/<ToDos.id>'
    path('yes_finish/<ToDos_id>', views.yes_finish, name = "yes_finish"),
    path('no_finish/<ToDos_id>', views.no_finish, name = "no_finish"),
    path('update/<ToDos_id>', views.update, name = "update"),
]
