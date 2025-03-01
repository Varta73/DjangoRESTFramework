from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from materials.models import Course, Lesson


class User(AbstractUser):
    # Пользователь
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите Вашу почту"
    )
    avatar = models.ImageField(
        upload_to="users/avatar/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    phone = models.CharField(
        max_length=12,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(max_length=50, verbose_name="Город", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    # Платежи
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    date_of_payment = models.DateField(
        verbose_name="Дата оплаты",
        blank=True,
        null=True,
        help_text="Укажите дату оплаты",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
        help_text="Введите сумму оплаты",
        null=True,
        blank=True,
    )
    FORM_PAYMENT_CHOICES = [
        ("перевод на счет", "наличные"),
    ]

    form_of_payment = models.CharField(
        max_length=200,
        verbose_name="Форма оплаты",
        choices=FORM_PAYMENT_CHOICES,
        default="перевод на счет",
        help_text="Укажите форму оплаты",
        null=True,
        blank=True,
    )

    session_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Id сессии",
        help_text="Укажите Id сессии",
    )
    link = models.URLField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Пользователь - {self.user}, оплатил {self.amount}"
