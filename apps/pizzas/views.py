from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from drf_yasg.utils import swagger_auto_schema

from .task import cook_pizza
from .models import Pizza
from .selectors import list_all_pizza
from .services import create_pizza
import logging

# from .serializers import PizzaSerializerpip


class GetPizzaListView(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'OutputListSerializer'
            model = Pizza
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='OutputListSerializer',
        responses={200: OutputSerializer()}
    )
    def get(self, request):
        queryset = list_all_pizza()
        serializer = self.OutputSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)


class GetPizzaView(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'OutputPizzaSerializer'
            model = Pizza
            fields = ('id', 'name', 'pastry', 'cheese', 'secret_ingredient', 'cooking_time', 'state',)

    @swagger_auto_schema(
        operation_description='OutputPizzaSerializer',
        responses={200: OutputSerializer()}
    )
    def get(self, request, *args, **kwargs):
        queryset = list_all_pizza()
        instance = queryset.get(pk=self.kwargs['pk'])
        serializer = self.OutputSerializer(instance)
        return Response(serializer.data, status=200)


class PostPizzaView(APIView):
    queryset = Pizza.objects.all()

    class InputPizzaSerializerPost(serializers.Serializer):
        name = serializers.CharField(max_length=128)
        pastry = serializers.CharField(max_length=2)
        cheese = serializers.CharField(max_length=128)
        secret_ingredient = serializers.CharField(max_length=128)
        cooking_time = serializers.FloatField(default=10)

        class Meta:
            ref_name = 'InputPizzaSerializerPost'

    class OutputPizzaSerializerPost(serializers.ModelSerializer):
        class Meta:
            ref_name = 'OutputPizzaSerializerPost'
            model = Pizza
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Create Pizza',
        request_body=InputPizzaSerializerPost(),
        responses={201: OutputPizzaSerializerPost()}
    )
    def post(self, request):
        serializer = self.InputPizzaSerializerPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        pizza = create_pizza(**serializer.validated_data)
        response_data = self.OutputPizzaSerializerPost(instance=pizza).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)


#
# class PatchPizzaView(APIView):
#     class InputPizzaSerializer(serializers.ModelSerializer):
#         class Meta:
#             ref_name = 'PizzaSerializer'
#             model = Pizza
#             fields = '__all__'
#
#     def update(self, request, *args, **kwargs):
#         queryset = list_all_pizza()
#         instance = queryset.get(pk=self.kwargs['pk'])
#         serializer = self.InputPizzaSerializer(instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)


class DeletePizza(APIView):
    queryset = list_all_pizza()

    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response(status=204)


class CookingPizza(APIView):
    # queryset = list_all_pizza()

    class InputPizzaSerializer(serializers.Serializer):
        id = serializers.IntegerField()

        class Meta:
            ref_name = 'InputPizzaSerializer'

    @swagger_auto_schema(
        operation_description='Cook Pizza',
        request_body=InputPizzaSerializer(),
    )
    def post(self, request):
        serializer = self.InputPizzaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        pizza_id = validated_data.get('id')
        logging.info(pizza_id)
        task = cook_pizza.delay(pizza_id=pizza_id)
        response_data = {
            'task_id': task.id,
            'task_status': task.state
        }
        return Response(data=response_data)
