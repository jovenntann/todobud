from django.utils import timezone
from typing import List

# Models
from ..models import Todo
from domain.guests.models import Guest

# UUID
import uuid

import logging
logger = logging.getLogger(__name__)


def get_todos() -> List[Todo]:
    todos = Todo.objects.all()
    logger.info(f"{todos} fetched")
    return todos


def get_todos_by_guest_id(guest_id: int) -> List[Todo]:
    guest = Guest.objects.filter(id=guest_id).first()
    todos = Todo.objects.filter(guest=guest).all()
    logger.info(f"{len(todos)} todos fetched for guest UUID: {guest_id}")
    return todos


def delete_todo(todo: Todo) -> Todo:
    todo.delete()
    logger.info(f"{todo} has been deleted.")
    return todo


def create_todo(
        guest: Guest,
        title: str,
        status: str,
        notes: str = None,
        due_date=None
) -> Todo:

    todo = Todo.objects.create(
        guest=guest,
        title=title,
        status=status,
        notes=notes,
        due_date=due_date
    )
    todo.save()

    logger.info(f"\"{todo.title}\" has been created")

    return todo


def create_todo_with_guest_id(
        guest_id: int,
        title: str,
        status: str,
        notes: str = None,
        due_date=None
) -> Todo:

    todo = Todo.objects.create(
        guest_id=guest_id,
        title=title,
        status=status,
        notes=notes,
        due_date=due_date
    )
    todo.save()

    logger.info(f"\"{todo.title}\" has been created")

    return todo


def update_todo(
        todo: Todo,
        title: str,
        status: str,
        notes: str = None,
        due_date=None
) -> Todo:
    todo.title = title
    todo.status = status
    todo.notes = notes
    todo.due_date = due_date
    todo.updated_at = timezone.now()

    todo.save()

    logger.info(f"\"{todo}\" has been updated.")

    return todo
