from .models import Pizza
from rest_framework.generics import get_object_or_404


def list_all_pizza(*, filters=None):
    qs = Pizza.objects.all()
    return qs


def get_pizza(*, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return pizza
