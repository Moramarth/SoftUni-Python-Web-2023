from django.core.exceptions import ValidationError


def first_letter_validation(value):
    if value[0].islower():
        raise ValidationError("Your name must start with a capital letter!")
