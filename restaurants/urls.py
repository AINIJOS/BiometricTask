from django.urls import path

from .views import RestaurantListView, RestaurantDetailView, PizzaListView, PizzaDetailView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view()),
    path('pizzas/', PizzaListView.as_view()),
    path('pizzas/<int:pk>/', PizzaDetailView.as_view()),
]