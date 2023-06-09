from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializerWithToken
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView


#Register
class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            user = User.objects.create(
                username = data["username"],
                # email = data["email"],
                password = make_password(data["password"])
            )
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {"detail": "user with this username already exists"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


#Login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#Coordinatess

class UpdatingCoordinates(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        profile = request.user.profile
        profile.current_coordinates = data["current_coordinates"]
        profile.save()
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)