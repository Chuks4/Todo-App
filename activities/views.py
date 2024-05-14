from django.shortcuts import render, redirect
from .forms import CreateTask
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def welcome(request):
    profile = request.user.profile
    notifications = profile.notification.filter(read=False).order_by("-created")
    context = {
        'notifications': notifications
    }
    return render(request, "welcome.html", context)


@login_required(login_url="login")
def createTask(request):
    owner = request.user.profile
    notifications = owner.notification.filter(read=False).order_by("-created")
    form = CreateTask()
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = owner
            task.save()
            messages.success(request, "Task was successfully created.")
            return redirect("tasks")

    context = {
        "form": form,
        'notifications': notifications
        }
    return render(request, "todo-form.html", context)


@login_required(login_url="login")
def updateTask(request, pk):
    owner = request.user.profile
    notifications = owner.notification.filter(read=False).order_by("-created")
    task = owner.tasks.get(id=pk)
    form = CreateTask(instance=task)
    if request.method == "POST":
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task was successfully updated.")
            return redirect("tasks")
    context = {
        "form": form,
        'notifications': notifications
        }
    return render(request, "todo-form.html", context)


@login_required(login_url="login")
def deleteTask(request, pk):
    owner = request.user.profile
    notifications = owner.notification.filter(read=False).order_by("-created")
    task = owner.tasks.get(id=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task was successfully deleted.")
        return redirect("tasks")
    context = {
        "task": task,
        'notifications': notifications
        }
    return render(request, "delete-template.html", context)


def tasks(request):
    profile = request.user.profile
    notifications = profile.notification.filter(read=False).order_by("-created")
    tasks = profile.tasks.all()
    context = {
        "tasks": tasks,
        'notifications': notifications
    }
    return render(request, "task.html", context)


def complete_task(request):
    profile = request.user.profile
    tasks = profile.tasks.all()
    done = True
    if request.method == "POST":
        for task in tasks:
            task_id = str(task.id)
            if task_id in request.POST:

                if not task.completed:
                    task.completed = True
                    if done:
                        messages.success(
                            request, "Congratulations! you just completed your task."
                        )
                        done = False

            else:
                task.completed = False
            task.save()
        return redirect("tasks")

    return render(request, "task.html")
    



