from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from staff.models import Trainer


class Program(models.Model):
    title = models.CharField(max_length=250)

    slug = AutoSlugField(
        populate_from='title',
        editable=False,
        always_update=True,
        unique=True,
        null=True,
        verbose_name='URL')

    image = models.ImageField(
        upload_to='programs')

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=350, height=250)],
        format='JPEG',
        options={'quality': 90})

    image_web = ImageSpecField(
        source='image',
        processors=[ResizeToFill(width=640, height=390)],
        format='JPEG',
        options={'quality': 90})

    youtube_id = models.CharField(
        max_length=100,
        help_text='Video ID from YouTube',
        blank=True,
        null=True)

    trainers = models.ManyToManyField(Trainer)

    description = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/program/' + self.slug + '/'


class Rank(models.Model):
    title = models.CharField(max_length=100)

    program = models.ForeignKey(Program)

    requirements = RichTextField(blank=True)

    def __str__(self):
        return self.title
