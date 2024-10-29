from django.contrib import admin
from . import models


class EleitorAdmin(admin.ModelAdmin):
    list_display = ('nomeeleitor', 'whatsapp',)
    search_fields = ('nomeeleitor',)


admin.site.register(models.Eleitor, EleitorAdmin)	

