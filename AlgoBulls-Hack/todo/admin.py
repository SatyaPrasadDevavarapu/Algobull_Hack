from django.contrib import admin
from .models import Todo, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # Display fields in the tag changelist view
    search_fields = ("name",)  # Add search functionality


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    # Fields displayed in the changelist view
    list_display = ("id", "title", "status", "due_date", "timestamp")
    # Add filters for changelist view
    list_filter = ("status", "tags", "due_date", "timestamp")
    # Add search functionality for title and description
    search_fields = ("title", "description")

    # Define fieldsets for detailed view
    fieldsets = (
        ("Basic Information", {"fields": ("title", "description", "status")}),
        ("Additional Information", {"fields": ("due_date", "tags")}),
        (
            "Read-only Fields",
            {
                "fields": ("timestamp",),
                "classes": ("collapse",),  # Collapse the section to save space
            },
        ),
    )

    # Make the timestamp field read-only
    readonly_fields = ("timestamp",)
