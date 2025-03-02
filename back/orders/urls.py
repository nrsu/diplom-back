from django.urls import path
from .views import add_to_cart, cart_detail

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
