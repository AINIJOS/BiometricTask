from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Restaurant, Pizza
from .serializers import RestaurantSerializer, PizzaSerializer


class RestaurantListView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.get_queryset(),
            many=True
        )
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class RestaurantDetailView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(
            instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        instance.delete()
        return Response(status=204)


class PizzaListView(GenericAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.get_queryset(),
            many=True
        )
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class PizzaDetailView(GenericAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(
            instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs['pk'])
        instance.delete()
        return Response(status=204)
