from rest_framework import serializers

# Models
from domain.todos.models import Todo

import logging
logger = logging.getLogger(__name__)


class ReadTodoSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "public.guests.todoss.ReadTodoSerializer"
        model = Todo
        fields = [
            'guest',
            'title',
            'status',
            'notes',
            'due_date',
            'created_at',
            'updated_at'
        ]


class CreateTodoSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "public.guests.todoss.CreateTodoSerializer"
        model = Todo
        fields = [
            'guest',
            'title',
            'status',
            'notes',
            'due_date'
        ]


class PaginateReadTodoSerializer(serializers.Serializer):  # noqa

    class Meta:
        ref_name = "public.guests.todoss.PaginateReadTodoSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadTodoSerializer(many=True)


class PaginateQueryReadTodoSerializer(serializers.Serializer):  # noqa
    class Meta:
        ref_name = "public.guests.todoss.PaginateQueryReadTodoSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
