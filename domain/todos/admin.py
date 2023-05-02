from django.contrib import admin

# Register your models here.
from .models import Todo

admin.site.site_header = 'Django Admin'
admin.site.site_title = 'Django Admin'
admin.site.index_title = 'Django Administration'


admin.site.register(Todo)

