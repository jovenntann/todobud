from rest_framework import serializers


import logging
logger = logging.getLogger(__name__)


class TodoSerializer(serializers.Serializer): # noqa
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=10)
    notes = serializers.CharField(max_length=500, allow_blank=True)
    due_date = serializers.DateField()


class ReadChatSerializer(serializers.Serializer): # noqa
    response = serializers.CharField(max_length=500)
    todos = TodoSerializer(many=True)


class CreateChatSerializer(serializers.Serializer): # noqa

    message = serializers.CharField()


class PaginateReadTodoSerializer(serializers.Serializer):  # noqa

    class Meta:
        ref_name = "public.guests.chats.PaginateReadTodoSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadChatSerializer(many=True)


class PaginateQueryReadTodoSerializer(serializers.Serializer):  # noqa
    class Meta:
        ref_name = "public.guests.chats.PaginateQueryReadTodoSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
