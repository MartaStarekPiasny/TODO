from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Category



class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Podaj email"
        })
    )

    username = forms.CharField(
        label="Nazwa użytkownika",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Podaj nazwę użytkownika"
        })
    )

    password1 = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Podaj hasło"
        })
    )

    password2 = forms.CharField(
        label="Powtórz hasło",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Powtórz hasło"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Użytkownik z takim adresem e-mail już istnieje.")

        return email


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["category"].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Task
        fields = ["title", "description", "category", "status", "priority", "due_date"]

        labels = {
            "title": "Tytuł",
            "description": "Opis",
            "category": "Kategoria",
            "status": "Status",
            "priority": "Priorytet",
            "due_date": "Termin",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Wpisz tytuł zadania"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Wpisz opis zadania"
            }),
            "category": forms.Select(attrs={
                "class": "form-select"
            }),
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
            "priority": forms.Select(attrs={
                "class": "form-select"
            }),
            "due_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        labels = {
            "name": "Nazwa kategorii",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Np. Hobby, Nauka, Zakupy"
            }),
        }