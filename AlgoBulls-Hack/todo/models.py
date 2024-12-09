from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )  # This ensures that tags are unique across all users.

    def __str__(self):
        return self.name


class Todo(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("WORKING", "Working"),
        ("PENDING REVIEW", "Pending Review"),
        ("COMPLETED", "Completed"),
        ("OVERDUE", "Overdue"),
        ("CANCELLED", "Cancelled"),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set on creation
    title = models.CharField(max_length=100)  # Mandatory
    description = models.TextField(max_length=1000)  # Mandatory
    due_date = models.DateField(null=True, blank=True)  # Optional
    tags = models.ManyToManyField(Tag, blank=True)  # Optional, many-to-many
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="OPEN"
    )  # Mandatory with default

    def __str__(self):
        return self.title
