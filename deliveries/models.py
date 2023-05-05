from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    coordinates = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    state = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="deliveries/meals/", null=True, blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    ingredient = models.ManyToManyField("Ingredient")

    def __str__(self):
        return self.name




class Ingredient(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class Restaurant_Types(models.Model):
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


