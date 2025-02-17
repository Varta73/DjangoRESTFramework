from django.db import models


class Course(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="static/images",
        verbose_name="Изображение",
        help_text="Загрузите фото курса",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="static/images",
        verbose_name="Изображение",
        help_text="Загрузите фото урока",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        "Course",
        verbose_name="Курс",
        on_delete=models.CASCADE,
        related_name="lessons",
        blank=True,
        null=True,
    )
    video_link = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
