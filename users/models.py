from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    address = models.TextField(max_length=300, blank=True)
    current_coordinates = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.user.username) + ' - ' + str(self.first_name) + ' ' + str(self.last_name)


