from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not all(char.isalpha() for char in value):
        raise ValidationError("Name must contain only letters")
