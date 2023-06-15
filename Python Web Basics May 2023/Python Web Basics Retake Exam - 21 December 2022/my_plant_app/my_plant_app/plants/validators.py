from django.core.exceptions import ValidationError


def only_letters_validation(value):
    if not all(char.isalpha() for char in value):
        raise ValidationError("Plant name should contain only letters!")
