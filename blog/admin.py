from django.contrib import admin
from blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Entry, EntryAdmin)
