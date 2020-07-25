from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"), # -2- views.index ---> todo_app in views dosyasında index isimli fonksiyon oluşturalım..
    path('about/', views.about, name = "about"), # -3- views.about ---> todo_app in views dosyasında index isimli fonksiyon oluşturalım..
    path('create/', views.create, name = "create"),
]

# -2- bu da bizi home index sayfamızda (hiçbirşeyin, 'about' gibi herhangi bir 
# uzantının olmadığı yerde ---> '' ---> bizi index e yönlendirir...

# http://127.0.0.1:8000/ --->>> index sayfası
# http://127.0.0.1:8000/admin/ --->>> admin sayfası --->>> http://127.0.0.1:8000/admin/login/