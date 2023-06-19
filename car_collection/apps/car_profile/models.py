from django.db import models
from django.core import validators


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        validators=[validators.MinLengthValidator(2, 'The username must be a minimum of 2 chars')]
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=[validators.MinValueValidator(18)]
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=30
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
