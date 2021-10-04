from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, FormView, DetailView
from .models import Todo
from .forms import TodoCreateForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages


class Home(ListView):
    template_name = "first/home.html"
    model = Todo
    context_object_name = "todos"
    ordering = ("-created",)


class DetailTodo(DetailView):
    template_name = "first/detail_todo.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(slug=self.kwargs['slug'])
        else:
            return Todo.objects.none()


class TodoCreate(FormView):
    form_class = TodoCreateForm
    template_name = "first/todo_create.html"
    success_url = reverse_lazy("first:home")

    def form_valid(self, form):
        self.create_todo(form.cleaned_data)
        return super().form_valid(form)

    def create_todo(self, data):
        todo = Todo(title=data['title'], slug=slugify(data['title']))
        todo.save()
        messages.success(self.request, "your todo added successfully", "success")
