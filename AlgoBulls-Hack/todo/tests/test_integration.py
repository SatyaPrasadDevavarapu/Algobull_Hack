# tests/test_integration.py
from rest_framework.test import APIClient
from django.test import TestCase
from todo.models import Todo, Tag


class TodoIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag = Tag.objects.create(name="Work")
        self.todo = Todo.objects.create(
            title="Finish Project",
            description="Complete the project by end of the day",
            status="OPEN",
        )
        self.todo.tags.add(self.tag)

    def test_create_and_get_todo(self):
        # Create Todo
        data = {
            "title": "New Todo",
            "description": "Test new todo",
            "status": "OPEN",
            "tags": [self.tag.id],
        }
        response = self.client.post("/api/todos/", data, format="json")
        self.assertEqual(response.status_code, 201)

        # Get Todo
        todo_id = response.data["id"]
        response = self.client.get(f"/api/todos/{todo_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "New Todo")
