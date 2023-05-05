from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RestaurantSerializer, SingleRestaurantSerializer, MealSerializer
from .models import Restaurant

from rest_framework.views import APIView
from rest_framework import generics

class SingleRestaurantView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        restaurant = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

class RestaurantListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = SingleRestaurantSerializer
    permission_classes = [AllowAny]