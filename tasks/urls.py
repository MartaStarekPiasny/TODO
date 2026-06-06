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

    path("categories/", views.categories, name="categories"),

    path("task/<int:task_id>/delete/", views.task_delete, name="task_delete"),
    path("task/<int:task_id>/toggle/", views.task_toggle, name="task_toggle"),
]
