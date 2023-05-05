---
#### domain/commons/models/__init__.py
```
from .Base import BaseModel

```

#### domain/commons/models/Base.py
```
from django.db import models

import logging
logger = logging.getLogger(__name__)


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
```

#### domain/users/models/__init__.py
```
from .Profile import Profile
from .Receiver import *

```

#### domain/users/models/Profile.py
```
from django.db import models
from domain.commons.models.Base import BaseModel
from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


class Profile(BaseModel):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):  # pragma: no cover
        return self.user.username

```

#### domain/todos/models/__init__.py
```
from .Todo import Todo

```

#### domain/todos/models/Todo.py
```
from django.db import models
from domain.commons.models.Base import BaseModel
from domain.guests.models.Guest import Guest

import logging

logger = logging.getLogger(__name__)


class Todo(BaseModel):

    id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('todo', 'To Do'), ('done', 'Done')], default='todo')
    notes = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):  # pragma: no cover
        return self.title

```

#### domain/guests/models/__init__.py
```
from .Guest import Guest

```

#### domain/guests/models/Guest.py
```
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

```
