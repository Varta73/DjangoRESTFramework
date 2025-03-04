import datetime
from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def user_block():
    """Блокировка пользователя при отсутствии активности в течение 30 дней"""
    month = timezone.now() - datetime.timedelta(days=30)
    users = User.objects.filter(last_login__lt=month).exclude(last_login__isnull=True)
    users.update(is_active=False)
    users.save()
