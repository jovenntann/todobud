from django.db import models
from domain.commons.models.Base import BaseModel
import logging

logger = logging.getLogger(__name__)


class Guest(BaseModel):

    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['id']

    def __str__(self):  # pragma: no cover
        return str(self.id)
