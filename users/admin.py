from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'is_staff')
    list_filter = ('programs', 'is_staff',)
    fieldsets = (
        (None, {
            'fields': (
                'username', 'first_name', 'last_name', 'is_staff',
                'is_active', 'programs')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'password', 'groups', 'user_permissions', 'last_login',
                'date_joined'),
        }),
    )


admin.site.register(User, UserAdmin)
