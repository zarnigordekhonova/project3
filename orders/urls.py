from django.urls import path
from orders.views import get_user_order

urlpatterns = [
    path('', get_user_order)
]