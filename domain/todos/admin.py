from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest', 'title', 'priority', 'status', 'notes', 'due_date', 'duration', 'time_spent')
    list_filter = ('status',)
    search_fields = ('title', 'notes')
    date_hierarchy = 'due_date'


admin.site.register(Todo, TodoAdmin)
