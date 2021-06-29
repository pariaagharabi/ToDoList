from collections import namedtuple
from django.urls import path
from .import views


urlpatterns = [
    path("<int:id>", views.todolist, name="todolist"),
    path("", views.home, name="home page"),
    path('<int:id>/edit/', views.edit, name="edit"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path("create/", views.create, name="create"),

]
