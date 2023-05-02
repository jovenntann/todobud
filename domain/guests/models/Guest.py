from django.db import models
from domain.commons.models.Base import BaseModel
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


class Guest(BaseModel):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):  # pragma: no cover
        return str(self.id)
