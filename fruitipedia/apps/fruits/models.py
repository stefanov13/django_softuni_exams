from django.db import models
from django.core import validators
from .validators import name_content_only_letter

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[validators.MinLengthValidator(2), name_content_only_letter],
        verbose_name='Fruit Name',
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Fruit Image URL',
    )

    description = models.TextField(
        blank=False,
        null=False,
        verbose_name=' Fruit Description',
    )

    nutrition = models.TextField(
        blank=True,
        null=True,
        verbose_name='Nutrition Info',
    )