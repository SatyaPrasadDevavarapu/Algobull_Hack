from rest_framework.exceptions import ValidationError
from django.test import TestCase
from todo.models import Todo, Tag
from todo.serializers import TodoSerializer


class TodoSerializerTest(TestCase):
    def test_todo_serializer_valid(self):
        tag = Tag.objects.create(name="Work")
        todo = Todo.objects.create(
            title="Finish Project",
            description="Complete the project by end of the day",
            status="OPEN",
        )
        todo.tags.add(tag)

        serializer = TodoSerializer(todo)
        self.assertEqual(serializer.data["title"], "Finish Project")

    def test_todo_serializer_invalid(self):
        data = {"title": "", "description": "Missing title", "status": "OPEN"}
        serializer = TodoSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
