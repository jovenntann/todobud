# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# Serializers
from .serializers import ReadChatSerializer, \
    CreateChatSerializer, PaginateReadTodoSerializer, \
    PaginateQueryReadTodoSerializer

# Models
from domain.todos.services.service_Todo import create_todo, create_todo_with_guest_id

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
            200: ReadChatSerializer()
        }
    )
    def post(request, guest_id):
        chat_serializer = CreateChatSerializer(data=request.data)
        chat_serializer.is_valid(raise_exception=True)

        response = ask_assistant(chat_serializer.validated_data.get('message', None))

        response_serializer = ReadChatSerializer(response)

        for todo in response_serializer.data['todos']:
            create_todo_with_guest_id(
                guest_id=guest_id,
                title=todo['title'],
                status=todo['status'],
                notes=todo['notes'],
                due_date=todo['due_date'],
            )

        return Response(response_serializer.data)
