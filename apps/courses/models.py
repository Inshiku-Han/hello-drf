from django.db import models

from apps.students.models import Student


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Course Title")
    description = models.TextField(blank=True, verbose_name="Course Description")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    students = models.ManyToManyField(
        Student, related_name="courses", verbose_name="Enrolled Students"
    )

    def __str__(self):
        return self.title
