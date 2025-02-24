from rest_framework.serializers import ValidationError

"""Проверка на использование ссылки только на yuotube.com."""


def validate_link(value):
    if "youtube.com" not in value.lower():
        raise ValidationError("Недопустимая ссылка")
