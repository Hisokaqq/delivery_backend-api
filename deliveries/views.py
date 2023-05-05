from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RestaurantSerializer, DetailedRestaurantSerializer, SearchedRestaurantSerializer, OrderSerializer
from .models import Restaurant, Order
from rest_framework.views import APIView
from rest_framework import generics


#RESTAURANTS
class RestaurantListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class SingleRestaurantView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        restaurant = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

class DetailedRestaurantDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        restaurant = Restaurant.objects.get(id=pk)
        serializer = DetailedRestaurantSerializer(restaurant)
        return Response(serializer.data)
    
class RestaurantSearchView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        search_query = request.query_params.get('search', '')
        restaurants = Restaurant.objects.filter(name__icontains=search_query)
        serializer = SearchedRestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class DetailedOrder(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
class OrdersList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)