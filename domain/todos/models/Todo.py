from django.db import models
from domain.commons.models.Base import BaseModel
from domain.guests.models.Guest import Guest

# Library: django-simple-history
from simple_history.models import HistoricalRecords

import logging

logger = logging.getLogger(__name__)


class Todo(BaseModel):

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='todo')
    notes = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(default=0, help_text="Duration in minutes")
    time_spent = models.PositiveIntegerField(default=0, help_text="Time spent in minutes")
    history = HistoricalRecords()

    class Meta:
        ordering = ['id']

    def __str__(self):  # pragma: no cover
        return self.title
