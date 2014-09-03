from django.contrib import admin

# Register your models here.
from .models import Champion, FightingType, ChampionFightingType


class ChampionFightingTypeInline(admin.TabularInline):
    model = ChampionFightingType
    extra = 1


class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_id',  'sex', 'partype')
    inlines = [ChampionFightingTypeInline]

admin.site.register(Champion, ChampionAdmin)
admin.site.register(FightingType)