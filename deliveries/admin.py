from django.contrib import admin
from .models import Restaurant, Order, Meal, Ingredient, Restaurant_Type, Meal_Type, Review

admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Restaurant_Type)
admin.site.register(Meal_Type)
admin.site.register(Review)
