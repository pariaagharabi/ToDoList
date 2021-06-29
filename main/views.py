from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import ToDoListForm
from django.contrib.auth.decorators import login_required

# redirect when user is not logged in
@login_required(login_url='/login/')
def todolist(request, id):
    # Get ToDoLost base on ID
    tdls = ToDoList.objects.filter(id=id, user=request.user)

    if tdls.count() == 0:
        errorMessage = f"to do list with id: {id} not found"
        return render(request, 'main/error.html', {"error": errorMessage})

    tdl = tdls[0]

    if request.method == "POST":
        if request.POST.get("save"):
            for item in tdl.item_set.all():
                if request.POST.get(f"c{item.id}") == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()
        elif request.POST.get("addItem"):
            txt = request.POST.get("newItem")
            if 2 < len(txt) < 30:
                tdl.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")

        else:
            for item in tdl.item_set.all():
                if request.POST.get(f"d{item.id}") == "delete":
                    item.delete()

    return render(request, 'main/todolists.html', {"tdl": tdl})


# redirect when user is not logged in
@login_required(login_url='/login/')
def home(request):
    tdls = None

    if request.user.is_authenticated:
        # tdls = ToDoList.objects.filter(user=request.user)
        # tdls = request.user.todolist_set.all()
        tdls = request.user.todolist.all()

    return render(request, 'main/home.html', {"tdls": tdls})

# redirect when user is not logged in
@login_required(login_url='/login/')
def edit(request, id):
    # tdl = ToDoList.objects.get(id=id)

    # if (tdl.user != request.user):
    #     errorMessage = f"To do list with id: {id} not found"
    #     return render(request, 'main/error.html', {"error": errorMessage})

    tdls = ToDoList.objects.filter(id=id, user=request.user)

    if tdls.count() == 0:
        errorMessage = f"To do list with id: {id} not found"
        return render(request, 'main/error.html', {"error": errorMessage})

    tdl = tdls[0]

    if request.method == "POST":
        print(request.POST)

        form = ToDoListForm(request.POST)

        if form.is_valid():
            form.instance.id = id
            form.save()

            return HttpResponseRedirect("/")

    form = ToDoListForm(instance=tdl)
    return render(request, 'main/edit.html', {"form": form})

# redirect when user is not logged in
@login_required(login_url='/login/')
def delete(request, id):
    tdls = ToDoList.objects.filter(id=id, user=request.user)

    if tdls.count() == 0:
        errorMessage = f"To do list with id: {id} not found"
        return render(request, 'main/error.html', {"error": errorMessage})

    tdls[0].delete()

    return HttpResponseRedirect("/")

# redirect when user is not logged in
@login_required(login_url='/login/')
def create(request):
    if request.method == "POST":
        form = ToDoListForm(request.POST)

        if form.is_valid():
            # tdl = ToDoList(name=form.cleaned_data['name'], user=request.user)
            # tdl.save()

            form.instance.user = request.user
            tdl = form.save()

            return HttpResponseRedirect(f"/{tdl.id}")

    form = ToDoListForm()
    return render(request, 'main/create.html', {"form": form})
