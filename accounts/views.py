from rest_framework import permissions, generics
from accounts.serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
