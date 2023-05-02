from django.contrib import admin
from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Guest, GuestAdmin)
