# urls.py
from django.urls import path
from .views import TodoListCreateView, TodoDetailView

urlpatterns = [
    path(
        "todos/", TodoListCreateView.as_view(), name="todo-list-create"
    ),  # List and create todos
    path(
        "todos/<int:pk>/", TodoDetailView.as_view(), name="todo-detail"
    ),  # Detail, update, delete todo by pk
]
