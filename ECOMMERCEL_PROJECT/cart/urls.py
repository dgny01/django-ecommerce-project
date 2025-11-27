from django.urls import path
from .views import AddToCartView, CartDetailView, CheckOutView
app_name = "cart"
urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'),
    path('add/<int:product_id>/',AddToCartView.as_view(),name="add-to-cart"),
    path('checkout/', CheckOutView.as_view(),name='checkout')
]
