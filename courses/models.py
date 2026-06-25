from django.db import models
from django.conf import settings


class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_title = models.CharField(max_length=200)
    credit = models.FloatField(default=3.0)

    # 🎯 ASSIGNED TEACHER
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'teacher'},
        related_name='assigned_courses'
    )

    def __str__(self):
        return f"{self.course_code} - {self.course_title}"