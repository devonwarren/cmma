from django.contrib import admin
from programs.models import Program, Rank


class RankAdmin(admin.ModelAdmin):
    list_display = ('title', 'program')


admin.site.register(Program)
admin.site.register(Rank, RankAdmin)
