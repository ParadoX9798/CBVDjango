from django.urls import path
from . import views

app_name = "first"
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('todo_create/', views.TodoCreate.as_view(), name="todo_create"),
    path('detail_todo/<slug:slug>/', views.DetailTodo.as_view(), name="detail_todo"),
    path('delete/<int:pk>/', views.DeleteTodo.as_view(), name="delete_todo"),

]
