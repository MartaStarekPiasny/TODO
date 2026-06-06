from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, TaskForm, CategoryForm
from .models import Task, Category
from datetime import date


@login_required
def index(request):
    categories = Category.objects.filter(user=request.user)
    selected_category_id = request.GET.get("category")

    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    selected_category = None

    if selected_category_id:
        selected_category = get_object_or_404(
            Category,
            id=selected_category_id,
            user=request.user
        )
        tasks = tasks.filter(category=selected_category)

    return render(request, "tasks/index.html", {
        "tasks": tasks,
        "categories": categories,
        "selected_category": selected_category,
        "today": date.today()
    })

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, user=request.user)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, "Zadanie zostało dodane.")
            return redirect("index")
    else:
        form = TaskForm(user=request.user)

    return render(request, "tasks/task_form.html", {
        "form": form
    })

@login_required
def category_create(request):
    next_url = request.GET.get("next") or request.POST.get("next") or "categories"

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()

            messages.success(request, "Kategoria została dodana.")
            return redirect(next_url)
    else:
        form = CategoryForm()

    return render(request, "tasks/category_form.html", {
        "form": form,
        "next": next_url
    })

@login_required
def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, "Kategoria została zaktualizowana.")
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)

    return render(request, "tasks/category_form.html", {
        "form": form,
        "category": category,
        "title": "Edytuj kategorię"
    })


@login_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)

    if request.method == "POST":
        category.delete()
        messages.success(request, "Kategoria została usunięta.")
        return redirect("categories")

    return render(request, "tasks/category_delete.html", {
        "category": category
    })

@login_required
def categories(request):
    categories = Category.objects.filter(user=request.user)

    return render(request, "tasks/categories.html", {
        "categories": categories
    })


@login_required
def category_tasks(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    tasks = Task.objects.filter(user=request.user, category=category)

    return render(request, "tasks/category_tasks.html", {
        "category": category,
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
        form = TaskForm(request.POST, instance=task, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Zadanie zostało zaktualizowane.")
            return redirect("task_detail", task_id=task.id)
    else:
        form = TaskForm(instance=task, user=request.user)

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
            user = form.save()

            Category.objects.create(name="Praca", user=user)
            Category.objects.create(name="Dom", user=user)
            Category.objects.create(name="Szkoła", user=user)

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