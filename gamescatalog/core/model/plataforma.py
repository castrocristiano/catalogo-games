from django.db import models

from core.model.jogo import Jogo


class Plataforma(models.Model):
    titulo = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho', max_length=50)
    plataforma_jogo = models.ManyToManyField(
        Jogo,
        through='PlataformaJogo',
        through_fields=('plataforma','jogo')
    )

    def __str__(self):
        return self.titulo
