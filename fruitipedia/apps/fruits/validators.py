from django.core.exceptions import ValidationError

def name_content_only_letter(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
    