# DRF
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from .serializers import OpenAiResponseSerializer, CreateChatSerializer

# Models
from domain.todos.services.service_Todo import create_todo_with_guest_id, \
    get_todos_by_guest_id, update_todo, get_todo_by_id, delete_todo

# Services
from domain.chatgpt.services.service_ChatGPT import ask_assistant

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class GuestsIdChatsAPIView(APIView):

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateChatSerializer,
        operation_description="description",
        operation_id="chats_create",
        tags=["public.guests.chats"],
        responses={
            200: OpenAiResponseSerializer()
        }
    )
    def post(request, guest_id):

        todos = get_todos_by_guest_id(guest_id)

        chat_serializer = CreateChatSerializer(data=request.data)
        chat_serializer.is_valid(raise_exception=True)
        message = chat_serializer.validated_data.get('message', None)

        openai_response = ask_assistant(question=message, todos=todos)

        openai_response_serializer = OpenAiResponseSerializer(data=openai_response)
        openai_response_serializer.is_valid(raise_exception=True)

        for todo_dict in openai_response_serializer.data['todos']:
            todo_id = todo_dict.get('id')
            action = todo_dict.get('action')
            title = todo_dict['title']
            status = todo_dict['status']
            notes = todo_dict['notes']
            due_date = todo_dict['due_date']

            if action == "insert":
                create_todo_with_guest_id(
                    guest_id=guest_id,
                    title=title,
                    status=status,
                    notes=notes,
                    due_date=due_date,
                )
            if action == "update":
                todo = get_todo_by_id(todo_id)
                if todo:
                    update_todo(
                        todo=todo,
                        title=title,
                        status=status,
                        notes=notes,
                        due_date=due_date,
                    )
            if action == "delete":
                todo = get_todo_by_id(todo_id)
                if todo:
                    delete_todo(todo)

        return Response(openai_response_serializer.data)
