from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


class Entry(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(
        populate_from='title',
        editable=False,
        always_update=True,
        unique=True,
        null=True,
        verbose_name='URL')

    pub_date = models.DateTimeField()

    body = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date',]
