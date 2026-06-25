from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, default='student')

    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True
    )

    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)