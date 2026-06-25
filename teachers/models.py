from django.conf import settings
from django.db import models

class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email} ({self.designation})"