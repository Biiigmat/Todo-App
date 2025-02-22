from django.contrib import admin
from .models import Task
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('title', 'image')
    search_fields = ('title',)
    fieldsets = (
        ('', {
            'fields': ('title', 'image', 'image_thumbnail', 'complete',
                       'deadline',)
        }),

        ('', {
            'fields': ('descriptions',)
        }),
    )


admin.site.register(Task, TaskAdmin)

