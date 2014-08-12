from django.contrib import admin

# Register your models here.
from .models import Champion, BasicParameters


admin.site.register(Champion)
admin.site.register(BasicParameters)