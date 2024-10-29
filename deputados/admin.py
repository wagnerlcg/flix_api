from django.contrib import admin
from . import models


class DeputadoAdmin(admin.ModelAdmin):
    list_display = ('nomedeputado', 'whatsapp',)
    search_fields = ('nomedeputado',)


admin.site.register(models.Deputado, DeputadoAdmin)	

