from django.db import models
from django.core import validators
from .validators import name_only_letters

class Plant(models.Model):
    CHOICES = (
        ('outdoor_plants', 'Outdoor Plants'),
        ('indoor_plants', 'Indoor Plants'),
    )


    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=14,
        choices=CHOICES,
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[validators.MinLengthValidator(2), name_only_letters],
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )
    