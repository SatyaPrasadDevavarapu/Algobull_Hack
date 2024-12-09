from django.test import TestCase
from todo.models import Todo, Tag


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Urgent")
        self.assertEqual(tag.name, "Urgent")


class TodoModelTest(TestCase):
    def test_todo_creation(self):
        tag = Tag.objects.create(name="Work")
        todo = Todo.objects.create(
            title="Finish Project",
            description="Complete the project by end of the day",
            status="OPEN",
        )
        todo.tags.add(tag)

        self.assertEqual(todo.title, "Finish Project")
        self.assertEqual(todo.status, "OPEN")
        self.assertIn(tag, todo.tags.all())
