from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RestaurantSerializer, DetailedRestaurantSerializer, SearchedRestaurantSerializer, OrderSerializer
from .models import Restaurant, Order, Meal, OrderItem
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

class OrderView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None):
        if pk is not None:
            order = Order.objects.get(id=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

# My Orders
class MyOrdersList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id=None):
        user = request.user
        if order_id is not None:
            try:
                order = Order.objects.get(pk=order_id, receiver=user)
                serializer = OrderSerializer(order)
                return Response(serializer.data)
            except Order.DoesNotExist:
                return Response({'error': 'Order not found'}, status=404)
        else:
            orders = Order.objects.filter(receiver=user)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        restaurant_id = data.get('restaurant')
        order_items = data.get('order_items', [])

        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({'error': 'Restaurant not found'}, status=404)

        order = Order.objects.create(
            restaurant=restaurant,
            receiver=user,
            subtotal=0,
            delivery_price=0,
            tax_price=0,
            full_price=0
        )

        for item_data in order_items:
            meal_id = item_data.get('meal')
            quantity = item_data.get('quantity')

            try:
                meal = Meal.objects.get(pk=meal_id)
            except Meal.DoesNotExist:
                return Response({'error': 'Meal not found'}, status=404)

            order_item = OrderItem.objects.create(
                order=order,
                meal=meal,
                quantity=quantity
            )

            order.subtotal += meal.price * quantity

        # Calculate other prices (delivery, tax, etc.) if needed

        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)
    
    
