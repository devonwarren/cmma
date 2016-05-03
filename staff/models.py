from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


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

    image = models.ImageField(upload_to='staff')

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=350, height=250)],
        format='JPEG',
        options={'quality': 90})

    about = RichTextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return '/staff/' + self.slug + '/'
