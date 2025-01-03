from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import Student
from .serializers import StudentSerializer


@extend_schema(tags=["Students"])
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
