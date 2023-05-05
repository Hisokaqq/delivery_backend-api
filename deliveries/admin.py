from django.contrib import admin
from .models import Restaurant, Delivery, Meal, Ingredient

admin.site.register(Restaurant)
admin.site.register(Delivery)
admin.site.register(Meal)
admin.site.register(Ingredient)
