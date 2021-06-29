from main.models import ToDoList
from django import forms
from .models import ToDoList

# class ToDoListForm(forms.Form):
# name = forms.CharField(label="Name", max_length=200)


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = ["user"]
        labels = {
            "name": "To do list name"
        }
