from django.contrib import admin

from core.model.game import Jogo, Plataforma, PlataformaJogo

admin.site.register(Jogo)
admin.site.register(Plataforma)
admin.site.register(PlataformaJogo)
