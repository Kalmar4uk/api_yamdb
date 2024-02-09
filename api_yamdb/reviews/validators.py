from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError


def validate_correct_username(data):
    if data.lower() == 'me':
        raise ValidationError(
            f'Никнэйм пользователя не должен быть {data}'
        )


validate_username = UnicodeUsernameValidator()
