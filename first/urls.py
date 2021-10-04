from django.urls import path
from . import views
app_name = "first"
urlpatterns = [
    path('', views.Home.as_view(), name="hello"),
    path('detail_todo/<slug:slug>/', views.DetailTodo.as_view(), name="detail_todo")
]
