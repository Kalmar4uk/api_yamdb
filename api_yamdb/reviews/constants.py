from django.conf import settings

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

USER_ROLES = (
    (USER, USER),
    (MODERATOR, MODERATOR),
    (ADMIN, ADMIN),
)

LEN_FIELD = {
    'MAX_LEN_USERNAME': 150,
    'MAX_LEN_EMAIL': 254,
    'MAX_LEN_ROLE': 16,
    'MAX_LEN_NAME_TIT_CAT_GEN': 256,
    'MAX_LEN_TEXT_REW_COM': 200,
    'MIN_VALUE_VALID': 1,
    'MAX_VALUE_VALID': 10
}

MAX_LEN_LEAD = 30

PATH_TO_FILE = f'{settings.BASE_DIR}/static/data/'
