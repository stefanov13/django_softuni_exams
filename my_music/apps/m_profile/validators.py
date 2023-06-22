from django.core.exceptions import ValidationError


def username_only_letters_nums_underscores(value):
    for char in value:
       if not char.isalnum() and not char == '_':
           raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
