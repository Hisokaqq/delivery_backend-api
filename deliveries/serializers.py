from rest_framework import serializers
from .models import Restaurant, Meal, Ingredient, Restaurant_Type, Order, Review, Meal_Type

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class Meal_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_Type
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True)
    categories = Meal_TypeSerializer(many=True)
    class Meta:
        model = Meal
        fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'zip', 'state', 'num_reviews', 'stars']

class DetailedRestaurantSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'coordinates', 'country', 'city', 'zip', 'state', 'num_reviews', 'stars', 'meals']

class SearchedRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name']

class OrderSerializer(serializers.ModelSerializer):
    restaurant = serializers.SerializerMethodField()
    meals = serializers.StringRelatedField(many=True)
    order_stamp_time = serializers.DateTimeField(format="%d %b, %H:%M")

    class Meta:
        model = Order
        fields = ('id', 'restaurant', 'meals', 'subtotal', 'delivery_price', 'tax_price', 'full_price', 'order_stamp_time')
    
    def get_restaurant(self, obj):
        return {"id": obj.restaurant.id, "name": obj.restaurant.name}
