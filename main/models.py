from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todolist", default=3)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.id} --> {self.name}"


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text
