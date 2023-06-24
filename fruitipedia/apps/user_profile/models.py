from django.db import models
from django.core import validators
from .validators import name_first_char_letter

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[validators.MinLengthValidator(2), name_first_char_letter],
        verbose_name='First Name',
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[validators.MinLengthValidator(1), name_first_char_letter],
        verbose_name='Last Name',
    )

    email = models.EmailField(
        blank=False,
        null=False,
        max_length=40,
        verbose_name='Email',
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[validators.MinLengthValidator(8)],
        verbose_name='Password',
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Image URL',
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
        verbose_name='Age',
    )