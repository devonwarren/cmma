from django.db import models
from django.contrib.auth.models import AbstractUser
from programs.models import Program


class User(AbstractUser):
    programs = models.ManyToManyField(
        Program,
        blank=True)
