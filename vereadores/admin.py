from django.contrib import admin
from . import models


class VereadorAdmin(admin.ModelAdmin):
    list_display = ('nomevereador', 'whatsapp',)
    search_fields = ('nomevereador',)


admin.site.register(models.Vereador, VereadorAdmin)	

