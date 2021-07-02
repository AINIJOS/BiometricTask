from rest_framework import serializers

from .models import Restaurant, Pizza


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address')


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'pastry', 'cheese', 'secret_ingredient', 'restaurant')
