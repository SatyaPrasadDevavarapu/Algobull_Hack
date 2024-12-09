# serializers.py

from rest_framework import serializers
from .models import Todo, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]  # Allow sending the ID or name of the tag


class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        many=True, required=False
    )  # Many-to-many relation with tags, optional field

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "tags",
            "status",
            "timestamp",
        ]

    def create(self, validated_data):
        # Extract tags data and create new tag instances if needed
        tags_data = validated_data.pop("tags", [])
        todo = Todo.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data["name"])
            todo.tags.add(tag)

        return todo

    def update(self, instance, validated_data):
        # Update the Todo object with new values
        tags_data = validated_data.pop("tags", [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update the tags
        instance.tags.clear()  # Remove all existing tags
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data["name"])
            instance.tags.add(tag)

        return instance
