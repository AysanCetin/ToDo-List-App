from django.contrib import admin

# Register your models here.
from .models import ToDos

admin.site.register(ToDos)