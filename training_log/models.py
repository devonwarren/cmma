from django.db import models
from users.models import User


class Entry(models.Model):
    student = models.ForeignKey(User)

    hours = models.DecimalField(decimal_places=2, max_digits=2)

    date = models.DateField(auto_now_add=True)

    description = models.CharField(max_length=250, blank=True)
