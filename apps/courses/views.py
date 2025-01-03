from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import Course
from .serializers import CourseSerializer


@extend_schema(tags=["Courses"])
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
