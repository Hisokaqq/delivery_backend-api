from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField("Restaurant_Type", blank=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    coordinates = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    state = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    num_reviews = models.IntegerField(blank=True)
    stars = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='meals')
    image = models.ImageField(upload_to="deliveries/meals/", null=True, blank=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    categories = models.ManyToManyField("Meal_Type", blank=True)
    description = models.TextField(max_length=200)
    ingredient = models.ManyToManyField("Ingredient")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class Restaurant_Type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class Meal_Type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
    delivery_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant + " delivering to " + self.receiver

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])




