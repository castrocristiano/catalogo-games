from django.db import models

from core.model.jogo import Jogo
from core.model.plataforma import Plataforma


class PlataformaJogo(models.Model):
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    slug = models.SlugField('Atalho')

    def __str__(self):
        return self.plataforma.__str__() + ' - ' + self.jogo.__str__()
