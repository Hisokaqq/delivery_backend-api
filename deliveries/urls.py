from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>', views.SingleRestaurantView.as_view(), name='restaurant'),
    path('restaurant-detail/<int:pk>', views.DetailedRestaurantDetailView.as_view(), name='detailed_restaurant'),
    path('restaurants/search/', views.RestaurantSearchView.as_view(), name='restaurant_search'),
    path('order/<int:pk>', views.DetailedOrder.as_view(), name='detailed_order'),
    path('orders/', views.OrdersList.as_view(), name='orders_list'),

]
