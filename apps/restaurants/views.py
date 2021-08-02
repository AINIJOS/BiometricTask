from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import serializers

from .models import Restaurant
from .selectors import list_all_restaurant
# from .serializers import queryset


class GetRestaurantListView(GenericAPIView):
    queryset = list_all_restaurant

    class PizzaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Restaurant
            fields = ('id', 'name', 'address',)

    def get(self, request, *args, **kwargs):
        serializer = self.PizzaSerializer(
            self.queryset(),
            many=True
        )
        return Response(serializer.data, status=200)


class GetRestaurantView(GenericAPIView):
    queryset = list_all_restaurant

    class PizzaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Restaurant
            fields = ('id', 'name', 'address',)

    def get(self, request, *args, **kwargs):
        instance = self.queryset().get(pk=self.kwargs['pk'])
        serializer = self.PizzaSerializer(instance)
        return Response(serializer.data)


class PutRestaurantView(GenericAPIView):
    queryset = list_all_restaurant

    class PizzaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Restaurant
            fields = ('id', 'name', 'address',)

    def put(self, request, *args, **kwargs):
        instance = self.queryset().get(pk=self.kwargs['pk'])
        serializer = self.PizzaSerializer(
            instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class PatchRestaurantView(GenericAPIView):
    queryset = list_all_restaurant

    class PizzaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Restaurant
            fields = ('id', 'name', 'address',)

    def patch(self, request, *args, **kwargs):
        instance = self.queryset().get(pk=self.kwargs['pk'])
        serializer = self.PizzaSerializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class DeleteRestaurantView(GetRestaurantView):
    queryset = list_all_restaurant

    def delete(self, request, *args, **kwargs):
        instance = self.queryset().get(pk=self.kwargs['pk'])
        instance.delete()
        return Response(status=204)
