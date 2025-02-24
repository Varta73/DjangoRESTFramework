from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons_from_course = SerializerMethodField()
    info_all_lessons_course = LessonSerializer(many=True, read_only=True)

    def get_count_lessons_from_course(self, course):
        # Количество уроков
        return Lesson.objects.filter(course=course).count()

    # def get_info_all_lessons_course(self, obj):
    #     # Все уроки связанные с курсом
    #     lessons = obj.lessons.all()
    #     return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons_from_course", "lessons")
