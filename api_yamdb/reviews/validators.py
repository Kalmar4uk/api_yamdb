from datetime import datetime as dt

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError


def validate_correct_username(data):
    if data.lower() == 'me':
        raise ValidationError(
            f'Никнэйм пользователя не должен быть {data}'
        )


def validate_year(data):
    if data > dt.now().year:
        raise ValidationError(
            'Год произведения не может быть больше текущего'
        )


validate_username = UnicodeUsernameValidator()
