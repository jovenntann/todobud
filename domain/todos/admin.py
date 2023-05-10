from django.contrib import admin
from .models import Todo
from simple_history.admin import SimpleHistoryAdmin


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest', 'title', 'priority', 'status', 'notes', 'due_date', 'duration', 'time_spent')
    list_filter = ('status',)
    search_fields = ('title', 'notes')
    date_hierarchy = 'due_date'


class TodoHistoryAdmin(TodoAdmin, SimpleHistoryAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(Todo, TodoHistoryAdmin)
