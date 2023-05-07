from rest_framework import serializers

# Models
from domain.todos.models import Todo

import logging
logger = logging.getLogger(__name__)


class ReadTodoSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "public.guests.todos.ReadTodoSerializer"
        model = Todo
        fields = [
            'id',
            'guest',
            'title',
            'priority',
            'status',
            'notes',
            'due_date',
            'duration',
            'time_spent',
            'created_at',
            'updated_at'
        ]


class CreateTodoSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "public.guests.todos.CreateTodoSerializer"
        model = Todo
        fields = [
            'guest',
            'title',
            'priority',
            'status',
            'notes',
            'due_date',
            'duration',
            'time_spent'
        ]


class PaginateReadTodoSerializer(serializers.Serializer):  # noqa

    class Meta:
        ref_name = "public.guests.todos.PaginateReadTodoSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadTodoSerializer(many=True)


class PaginateQueryReadTodoSerializer(serializers.Serializer):  # noqa
    class Meta:
        ref_name = "public.guests.todos.PaginateQueryReadTodoSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
