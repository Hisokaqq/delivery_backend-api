import os
from django.core.management.base import BaseCommand
from deliveries.models import Ingredient
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Create some Ingredients'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ingredients.txt')
        with open(file_path, 'r') as f:
            ingredients = f.read().split(', ')
            for name in ingredients:
                name = name.strip()
                try:
                    Ingredient.objects.create(name=name)
                    self.stdout.write(self.style.SUCCESS(f'Ingredient {name} created successfully.'))
                except IntegrityError:
                    self.stdout.write(self.style.WARNING(f'Ingredient {name} already exists. Skipping.'))
