from django.db import models
from ckeditor.fields import RichTextField
from programs.models import Program


class Rank(models.Model):
    title = models.CharField(max_length=100)

    program = models.ForeignKey(Program)

    requirements = RichTextField(blank=True)
