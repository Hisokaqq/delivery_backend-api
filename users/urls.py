from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('coordinates/', views.UpdatingCoordinates.as_view(), name='coordinates'),
    ]
