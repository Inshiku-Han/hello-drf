from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Registration Date"
    )

    def __str__(self):
        return self.name
