from __future__ import unicode_literals

from django.db import models
from apps.author.models import Author

class Post(models.Model):

    title = models.CharField(
        max_length = 255,
        help_text = "Titulo"
    )

    autor = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        help_text = "Autor"
    )

    '''
    image = models.ImageField(
        upload_to = "images/post",
        help_text = "imagen"
    )
    '''

    content = models.TextField(
        help_text = "Contenido"
    )

    publication_date = models.DateTimeField(
        help_text = "Fecha"
    )

    status = models.BooleanField(
        help_text = "Estado",
        default = True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
