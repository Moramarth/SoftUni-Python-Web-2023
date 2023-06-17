from django.core.exceptions import ValidationError
import re


def username_validation(username):
    pattern = "[A-Za-z0-9_]+"
    match = re.findall(pattern, username)
    if len(match[0]) != len(username) or len(match) != 1:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")