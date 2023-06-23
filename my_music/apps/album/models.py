from django.db import models
from django.core import validators

# Create your models here.
class Album(models.Model):
    CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )

    album_name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=30,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    genre = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        choices=CHOICES
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[validators.MinValueValidator(0)],
    )