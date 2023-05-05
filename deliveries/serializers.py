from rest_framework import serializers
from .models import Restaurant, Meal, Ingredient, Restaurant_Type, Delivery, Review, Meal_Type

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

class SingleRestaurantSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'coordinates', 'country', 'city', 'zip', 'state', 'num_reviews', 'stars', 'meals']

