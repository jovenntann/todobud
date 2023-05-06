from rest_framework import serializers


import logging
logger = logging.getLogger(__name__)


class TodoSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "public.guests.chats.TodoSerializer"

    id = serializers.IntegerField(allow_null=True, required=False)
    action = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=20)
    notes = serializers.CharField(max_length=500, allow_blank=True)
    due_date = serializers.DateField()



class OpenAiResponseSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "public.guests.chats.OpenAiResponseSerializer"

    response = serializers.CharField(max_length=500, allow_blank=True, allow_null=True)
    todos = TodoSerializer(many=True)


class CreateChatSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "public.guests.chats.CreateChatSerializer"

    message = serializers.CharField()
