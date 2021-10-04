from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Todo


class Home(TemplateView):
    template_name = "first/hello.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['todos'] = Todo.objects.all()
