from django import forms
from .models import ToDos

class ListForm(forms.ModelForm):
    class Meta:
        model = ToDos
        fields = ["title","description","finished","date"]

        