from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


class Trainer(models.Model):
    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    slug = AutoSlugField(
        populate_from='__str__',
        editable=False,
        always_update=True,
        unique=True,
        null=True,
        verbose_name='URL')

    about = RichTextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return '/staff/' + self.slug + '/'
