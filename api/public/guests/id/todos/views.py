# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# Serializers
from .serializers import ReadTodoSerializer, \
    CreateTodoSerializer, PaginateReadTodoSerializer, \
    PaginateQueryReadTodoSerializer

# Services
from domain.todos.services.service_Todo import get_todos, create_todo, get_todos_by_guest_id

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class GuestsIdTodosAPIView(APIView):

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadTodoSerializer()
        },
        operation_id="todos_list",
        tags=["public.guests.todos"],
        query_serializer=PaginateQueryReadTodoSerializer()
    )
    def get(request, guest_id):
        logging.info(guest_id)
        todos = get_todos_by_guest_id(guest_id)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(todos, request)
        todo_serializer = ReadTodoSerializer(result_page, many=True)
        return paginator.get_paginated_response(todo_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateTodoSerializer,
        operation_description="description",
        operation_id="todos_create",
        tags=["public.guests.todos"],
        responses={
            200: ReadTodoSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        todo_serializer = CreateTodoSerializer(data=request.data)
        todo_serializer.is_valid(raise_exception=True)
        todo = create_todo(
            todo_serializer.validated_data['guest'],
            todo_serializer.validated_data['title'],
            todo_serializer.validated_data['status'],
            todo_serializer.validated_data.get('notes', None),
            todo_serializer.validated_data.get('due_date', None),
        )
        todo_serializer = ReadTodoSerializer(todo)
        return Response(todo_serializer.data)
