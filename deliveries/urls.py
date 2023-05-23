from django.urls import path
from . import views

urlpatterns = [

    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>', views.SingleRestaurantView.as_view(), name='restaurant'),
    path('restaurant-detail/<int:pk>/', views.DetailedRestaurantDetailView.as_view(), name='detailed_restaurant'),
    path('restaurants/search/', views.RestaurantSearchView.as_view(), name='restaurant_search'),
    # Orders
    path('orders/', views.OrderView.as_view(), name='orders'),
    path('order/<int:pk>/', views.OrderView.as_view(), name='order'),
    # My Orders
    path('my/orders/', views.MyOrdersList.as_view(), name='my_orders_list'),
    path('my/orders/create/', views.MyOrdersList.as_view(), name='create_order'),
    path('my/orders/<int:order_id>/', views.MyOrdersList.as_view(), name='retrieve_order'),

]
