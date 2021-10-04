from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .models import Todo
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.contrib import messages
from .forms import CommentForm
from .models import Comment


class Home(ListView):
    template_name = "first/home.html"
    model = Todo
    context_object_name = "todos"
    ordering = ("-created",)


class DetailTodo(LoginRequiredMixin, FormMixin, DetailView):
    template_name = "first/detail_todo.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    model = Todo
    form_class = CommentForm

    def get_success_url(self):
        return reverse("first:detail_todo", kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = Comment(todo=self.object, name=form.cleaned_data['name'], body=form.cleaned_data['body'])
            comment.save()
        return super().form_valid(form)


# class TodoCreate(FormView):
#     form_class = TodoCreateForm
#     template_name = "first/todo_create.html"
#     success_url = reverse_lazy("first:home")
#
#     def form_valid(self, form):
#         self.create_todo(form.cleaned_data)
#         return super().form_valid(form)
#
#     def create_todo(self, data):
#         todo = Todo(title=data['title'], slug=slugify(data['title']))
#         todo.save()
#         messages.success(self.request, "your todo added successfully", "success")

class TodoCreate(CreateView):
    model = Todo
    fields = ('title',)
    template_name = "first/todo_create.html"
    success_url = reverse_lazy("first:home")

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, "your todo added successfully", "success")
        return super().form_valid(form)


class DeleteTodo(DeleteView):
    template_name = "first/delete_todo.html"
    model = Todo
    success_url = reverse_lazy("first:home")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "todo deleted successfully", "danger")
        return super(DeleteTodo, self).delete(request, *args, **kwargs)


class EditTodo(UpdateView):
    model = Todo
    fields = ('title',)
    template_name = "first/edit_todo.html"
    success_url = reverse_lazy("first:home")
