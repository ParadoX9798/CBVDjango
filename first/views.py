from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo


# class Home(TemplateView):
#     template_name = "first/hello.html"
#
#     def get_context_data(self, **kwargs):
#         contex = super().get_context_data(**kwargs)
#         contex['todos'] = Todo.objects.all()
#         return contex


class Home(ListView):
    template_name = "first/hello.html"
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
