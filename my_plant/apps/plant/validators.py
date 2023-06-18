from django.core.exceptions import ValidationError

def name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')