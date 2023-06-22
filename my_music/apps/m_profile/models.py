from django.db import models
from django.core import validators
from .validators import username_only_letters_nums_underscores

# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[validators.MinLengthValidator(2), username_only_letters_nums_underscores]
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[validators.MinValueValidator(0)],
    )
    