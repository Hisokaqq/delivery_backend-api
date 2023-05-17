import os
from django.core.management.base import BaseCommand
from deliveries.models import Ingredient, Restaurant, Meal, Restaurant_Type, Meal_Type

class Command(BaseCommand):
    help = 'Create McDonald\'s restaurant with full menu'

    def handle(self, *args, **options):
        # Create Restaurant
        mcdonalds = Restaurant.objects.create(
            owner_id=1,  # Replace with the appropriate owner ID
            name='McDonald\'s',
            address='123 Main St',
            phone_number='1234567890',
            coordinates='40.7128° N, 74.0060° W',
            country='USA',
            city='New York',
            zip='10001',
            state='NY',
            num_reviews=0,
            stars=0.0
        )

        # Create Ingredients
        ingredient_names = ['Beef Patty', 'Bun', 'Lettuce', 'Tomato', 'Cheese', 'Onion', 'Pickles', 'Ketchup', 'Mustard']
        try:
            ingredients = [Ingredient.objects.create(name=name) for name in ingredient_names]
        except:
            pass

        # Create Meal Types
        meal_type_names = ['Burger', 'Sandwich', 'Salad']
        meal_types = [Meal_Type.objects.create(name=name) for name in meal_type_names]

        # Create Meals
        meal_data = [
            {
                'name': 'Big Mac',
                'price': 5.99,
                'description': 'Two all-beef patties, special sauce, lettuce, cheese, pickles, onions on a sesame seed bun',
                'ingredient_ids': [1, 2, 3, 5, 6, 7, 8]
            },
            {
                'name': 'Cheeseburger',
                'price': 2.49,
                'description': 'Beef patty, cheese, pickles, onions, ketchup, mustard on a bun',
                'ingredient_ids': [1, 2, 5, 6, 7, 8, 9]
            },
            # Add more meals as needed
        ]

        for meal in meal_data:
            ingredients = Ingredient.objects.filter(pk__in=meal['ingredient_ids'])
            new_meal = Meal.objects.create(
                restaurant=mcdonalds,
                name=meal['name'],
                price=meal['price'],
                description=meal['description']
            )
            new_meal.ingredient.set(ingredients)
            new_meal.categories.set(meal_types)

        self.stdout.write(self.style.SUCCESS('McDonald\'s restaurant and menu created successfully.'))
