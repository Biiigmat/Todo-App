import admin_thumbnails
from django.contrib import admin
from .models import User


@admin_thumbnails.thumbnail('image')
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'image_thumbnail', 'is_superuser',)
    fieldsets = (
        ('Identifications ', {
            'fields': ('user_name', 'image', 'image_thumbnail', 'email',
                       'password', 'first_name', 'last_name',)
        }),

        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
    )
    search_fields = ('user_name', )
    ordering = ('user_name',)



admin.site.register(User, UserAdmin)
