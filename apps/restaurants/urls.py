from django.urls import path

from apps.restaurants.views import *

urlpatterns = [
    path('', GetRestaurantListView.as_view()),
    path('/<int:pk>/', GetRestaurantView.as_view()),
    path('/<int:pk>/put/', PutRestaurantView.as_view()),
    path('/<int:pk>/patch/', PatchRestaurantView.as_view()),
    path('/<int:pk>/delete/', DeleteRestaurantView.as_view()),

]
