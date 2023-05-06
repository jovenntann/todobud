from django.db import models
from domain.commons.models.Base import BaseModel
from domain.guests.models.Guest import Guest

import logging

logger = logging.getLogger(__name__)


class Todo(BaseModel):

    id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done')
    ], default='todo')
    notes = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):  # pragma: no cover
        return self.title
