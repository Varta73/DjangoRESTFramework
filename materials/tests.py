from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User
from rest_framework import status
from django.urls import reverse


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.com")
        self.course = Course.objects.create(name="Химия", description="Органическая")
        self.lesson = Lesson.objects.create(
            name="Белки", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("description"), self.lesson.description)

    def test_lesson_create(self):
        url = reverse(
            "materials:lesson_create",
        )

        data = {
            "name": "Урок 1",
            "course": self.course.pk,
            "video_link": "https://www.youtube.com",
            "owner": self.user.pk,
        }

        response = self.client.post(url, data)
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Урок 2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Урок 2")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_link": None,
                    "name": "Белки",
                    "description": None,
                    "image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@mail.com")
        self.course = Course.objects.create(name="Химия", description="Органическая")
        self.lesson = Lesson.objects.create(
            name="Белки", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("materials:subscription")
        response = self.client.post(url, {"course": self.course.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка добавлена")
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

        url = reverse("materials:subscription")
        response = self.client.post(url, {"course": self.course.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка удалена")
        self.assertFalse(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )
