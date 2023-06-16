from django.core.exceptions import ValidationError

def name_first_letter_capital(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')