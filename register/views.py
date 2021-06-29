from django.shortcuts import render, redirect
from .forms import RegisterationForm


def register(response):
    if response.method == "POST":
        form = RegisterationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterationForm()

    return render(response, "register/register.html", {"form": form})
