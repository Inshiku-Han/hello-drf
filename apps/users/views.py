from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework_simplejwt import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import UserLoginSerializer, UserRegisterSerializer


@extend_schema(tags=["Users"])
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer


@extend_schema(tags=["Users"])
class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            tokens = serializer.save()
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Users"])
class RefreshView(views.TokenRefreshView):
    pass
