from django.urls import path

from .views import *

urlpatterns = [
    path('', GetPizzaListView.as_view()),
    path('cook/', CookingPizza.as_view()),
    path('<int:pk>/', GetPizzaView.as_view()),
    path('create/', PostPizzaView.as_view()),
    # path('/<int:pk>/patch/', PatchPizzaView.as_view()),
    path('<int:pk>/delete/', DeletePizza.as_view()),

]
