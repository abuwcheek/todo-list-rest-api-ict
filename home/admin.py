from django.contrib import admin
from .models import Tasks



@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
     list_display = ['title', 'task_time', 'created', 'updated', 'complete', ]
     list_display_links = ['title', 'task_time', 'created',]
     search_fields = ['title']
     list_editable = ['complete']