from django.utils import timezone
from typing import List

# Models
from ..models import Todo
from domain.guests.models import Guest


import logging
logger = logging.getLogger(__name__)


def get_todo_by_id(todo_id: int) -> Todo:
    todo = Todo.objects.filter(id=todo_id).first()
    logger.info(f"Todo with ID {todo_id} fetched")
    return todo


def get_todos() -> List[Todo]:
    todos = Todo.objects.all()
    logger.info(f"{todos} fetched")
    return todos


def get_todos_by_guest_id(guest_id: int) -> List[Todo]:
    guest = Guest.objects.filter(id=guest_id).first()
    todos = Todo.objects.filter(guest=guest).order_by('-updated_at').all()
    logger.info(f"{len(todos)} todos fetched for guest id: {guest_id}")
    return todos


def delete_todo(todo: Todo) -> Todo:
    todo.delete()
    logger.info(f"{todo} has been deleted.")
    return todo


def create_todo(
        guest: Guest,
        title: str,
        priority: str,
        status: str,
        notes: str = None,
        due_date=None,
        duration: int = 0,
        time_spent: int = 0
) -> Todo:

    todo = Todo.objects.create(
        guest=guest,
        title=title,
        priority=priority,
        status=status,
        notes=notes,
        due_date=due_date,
        duration=duration,
        time_spent=time_spent,
    )
    todo.save()

    logger.info(f"\"{todo.title}\" has been created")

    return todo


def create_todo_with_guest_id(
        guest_id: int,
        title: str,
        priority: str,
        status: str,
        notes: str = None,
        due_date: int = None,
        duration: int = None,
        time_spent: int = None,
) -> Todo:

    todo = Todo.objects.create(
        guest_id=guest_id,
        title=title,
        priority=priority,
        status=status,
        notes=notes,
        due_date=due_date,
        duration=duration,
        time_spent=time_spent
    )
    todo.save()

    logger.info(f"\"{todo.title}\" has been created")

    return todo


def update_todo(
        todo: Todo,
        title: str,
        priority: str,
        status: str,
        notes: str = None,
        due_date: int = None,
        duration: int = None,
        time_spent: int = None,
) -> Todo:
    todo.title = title
    todo.priority = priority
    todo.status = status
    todo.notes = notes
    todo.due_date = due_date
    todo.duration = duration
    todo.time_spent = time_spent
    todo.updated_at = timezone.now()

    todo.save()

    logger.info(f"\"{todo}\" has been updated.")

    return todo
