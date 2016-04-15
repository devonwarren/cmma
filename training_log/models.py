from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Entry(models.Model):
    student = models.ForeignKey(User)

    hours = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0.1), MaxValueValidator(24)])

    date = models.DateField()

    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return '/accounts/log/' + str(self.id)

    class Meta:
        get_latest_by = 'date'
