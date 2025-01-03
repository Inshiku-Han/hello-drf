from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.students.models import Student


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, null=True, blank=True, related_name="user"
    )
