from django.core.exceptions import ValidationError


def year_range_validation(value):
    if not 1980 <= value <= 2049:
        raise "Year must be between 1980 and 2049"
