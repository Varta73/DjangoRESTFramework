from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@shared_task
def send_information_about_update(email, message):
    """Уведомление об обновлении курса"""

    send_mail('Обновление материалов курса', message, EMAIL_HOST_USER, [email])