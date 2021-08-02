from .models import Pizza


def create_pizza(**kwargs):
    pizza = Pizza(**kwargs)
    pizza.save()
    return pizza
