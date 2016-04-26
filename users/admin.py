from django.contrib import admin
from users.models import User
from training_log.models import Entry


class EntryInline(admin.StackedInline):
    model = Entry
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    list_filter = ('programs', 'is_staff',)
    fieldsets = (
        (None, {
            'fields': (
                'username', 'first_name', 'last_name', 'email', 'is_staff',
                'is_active', 'programs', 'ranks')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'password', 'groups', 'user_permissions', 'last_login',
                'date_joined'),
        }),
    )
    inlines = [EntryInline]



admin.site.register(User, UserAdmin)
