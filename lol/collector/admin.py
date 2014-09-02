from django.contrib import admin

# Register your models here.
from .models import Champion


class ChampionAdmin(admin.ModelAdmin):
    list_display = ('champion_id', 'name', 'sex', 'partype')

admin.site.register(Champion, ChampionAdmin)
