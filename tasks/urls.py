from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),

    path("task/new/", views.task_create, name="task_create"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("task/<int:task_id>/edit/", views.task_edit, name="task_edit"),
    path("task/<int:task_id>/delete/", views.task_delete, name="task_delete"),
    path("task/<int:task_id>/toggle/", views.task_toggle, name="task_toggle"),
    path("categories/new/", views.category_create, name="category_create"),
    path("categories/", views.categories, name="categories"),
    path("categories/<int:category_id>/", views.category_tasks, name="category_tasks"),
    path("categories/<int:category_id>/edit/", views.category_edit, name="category_edit"),
    path("categories/<int:category_id>/delete/", views.category_delete, name="category_delete"),
]
