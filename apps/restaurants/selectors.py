from .models import Restaurant


def list_all_restaurant(*, filters=None):
    qs = Restaurant.objects.all()
    return qs

