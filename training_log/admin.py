from django.contrib import admin
from training_log.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'hours', 'description')
    list_filter = ('student', 'date',)


admin.site.register(Entry, EntryAdmin)
