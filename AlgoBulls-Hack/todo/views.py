# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Import the permission class
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]  # Ensure authentication


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]  # Ensure authentication
