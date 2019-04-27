from __future__ import unicode_literals

from django.db import models

class Author(models.Model):

    name = models.CharField(
        max_length = 255,
        help_text = "Nombre"
    )

    '''
    image = models.ImageField(
        upload_to = "images/author",
        blank=True, 
        null=True
    )
    '''

    description = models.TextField(
        help_text = "Descripcion"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'