from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import LessonViewSet
from materials.apps import MaterialsConfig
from materials.views import (
    CourseListAPIView,
    CourseCreateAPIView,
    CourseUpdateAPIView,
    CourseDestroyAPIView,
    CourseRetrieveAPIView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", LessonViewSet)

urlpatterns = [
    path("course/", CourseListAPIView.as_view(), name="course_list"),
    path("course/create/", CourseCreateAPIView.as_view(), name="course_create"),
    path("course/<int:pk>/", CourseRetrieveAPIView.as_view(), name="course_retrieve"),
    path(
        "course/<int:pk>/delete/", CourseDestroyAPIView.as_view(), name="course_delete"
    ),
    path(
        "course/<int:pk>/update/", CourseUpdateAPIView.as_view(), name="course_update"
    ),
]

urlpatterns += router.urls
