from django.db import models
from django.core import validators
from .validators import valid_car_year

# Create your models here.
class Car(models.Model):
    CHOICES = (
        ('sports_car', 'Sports Car'),
        ('pickup', 'Pickup'),
        ('crossover', 'Crossover'),
        ('minibus', 'Minibus'),
        ('other', 'Other'),
    )

    type = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        choices=CHOICES,
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[validators.MinLengthValidator(2)],
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[valid_car_year]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[validators.MinValueValidator(1)],
    )
    