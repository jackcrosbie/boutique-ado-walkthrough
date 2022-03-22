from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name="checkout"),
    # take order number as argument
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]
