from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, TaskForm
from .models import Task
from datetime import date

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "tasks/index.html", {
        "tasks": tasks,
        "today": date.today()
    })


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, "Zadanie zostało dodane.")
            return redirect("index")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {
        "form": form
    })


@login_required
def categories(request):
    tasks = Task.objects.filter(user=request.user)

    return render(request, "tasks/categories.html", {
        "tasks": tasks
    })


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    return render(request, "tasks/task_detail.html", {
        "task": task
    })

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Zadanie zostało zaktualizowane.")
            return redirect("task_detail", task_id=task.id)
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_edit.html", {
        "form": form,
        "task": task
    })

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Zadanie zostało usunięte.")
        return redirect("index")

    return render(request, "tasks/task_delete.html", {
        "task": task
    })

@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    task.is_completed = not task.is_completed
    task.save()

    return redirect("index")


def register(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Konto zostało utworzone. Możesz się zalogować.")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "tasks/register.html", {
        "form": form
    })


class CustomLoginView(LoginView):
    template_name = "tasks/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    pass