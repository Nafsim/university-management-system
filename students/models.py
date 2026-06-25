from django.conf import settings
from django.db import models

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField(default=1)
    cgpa = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.email} ({self.student_id})"