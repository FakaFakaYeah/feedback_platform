from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(value):
    if str.lower(value) == 'me':
        raise ValidationError('Нельзя создавать пользователя с такими именем!')


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError('Укажите правильный год произведения!')
