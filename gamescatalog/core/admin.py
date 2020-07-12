from django.contrib import admin

from core.model.jogo import Jogo
from core.model.plataforma import Plataforma
from core.model.plataforma_jogo import PlataformaJogo


class JogoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'id']
    prepopulated_fields = {'slug': ['titulo']}


class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'id']
    prepopulated_fields = {'slug': ['titulo']}


class PlataformaJogoAdmin(admin.ModelAdmin):
    list_display = ['plataforma', 'jogo', 'slug']
    prepopulated_fields = {'slug': ['plataforma', 'jogo']}


admin.site.register(Jogo, JogoAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(PlataformaJogo, PlataformaJogoAdmin)
