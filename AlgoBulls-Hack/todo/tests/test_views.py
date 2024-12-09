# tests/test_views.py
from rest_framework.test import APIClient
from django.test import TestCase
from todo.models import Todo, Tag


class TodoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag = Tag.objects.create(name="Work")
        self.todo = Todo.objects.create(
            title="Finish Project",
            description="Complete the project by end of the day",
            status="OPEN",
        )
        self.todo.tags.add(self.tag)

    def test_get_todos(self):
        response = self.client.get("/api/todos/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", response.data[0])

    def test_create_todo(self):
        data = {
            "title": "New Todo",
            "description": "Test new todo",
            "status": "OPEN",
            "tags": [self.tag.id],
        }
        response = self.client.post("/api/todos/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "New Todo")

    def test_update_todo(self):
        data = {
            "title": "Updated Todo",
            "description": "Updated description",
            "status": "COMPLETED",
            "tags": [self.tag.id],
        }
        response = self.client.put(f"/api/todos/{self.todo.id}/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Updated Todo")

    def test_delete_todo(self):
        response = self.client.delete(f"/api/todos/{self.todo.id}/")
        self.assertEqual(response.status_code, 204)
