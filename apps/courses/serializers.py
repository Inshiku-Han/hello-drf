from rest_framework import serializers

from .models import Course
from apps.students.serializers import StudentSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course model"""

    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "start_date", "end_date", "students"]
