from apps.taskapp.celery import celery_app
from .selectors import *
import time
import logging

@celery_app.task
def cook_pizza(pizza_id):
    logging.info(pizza_id)
    pizza = get_pizza(pizza_id=pizza_id)
    print(pizza)
    if pizza.state == 'RAW':
        logging.info('if condition')
        time.sleep(pizza.cooking_time)
        pizza.state = 'DONE'
        pizza.save()
        print(' ! ' * 30)
        pizza.refresh_from_db()
        logging.info(pizza)
    print(' ! ' * 30)
    logging.info(vars(pizza))

