from django.db import models
from django.core import validators
from .validators import name_first_letter_capital

# Create your models here.
class Plant(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[validators.MaxLengthValidator(2)],
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[name_first_letter_capital],
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[name_first_letter_capital],
    )

    profile_picture = models.URLField(blank=True, null=True)
    