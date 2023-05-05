from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>', views.SingleRestaurantView.as_view(), name='restaurant'),
    path('restaurant-detail/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
]
