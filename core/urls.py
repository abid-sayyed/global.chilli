from django.urls import path
from .views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    ProductDetailView,
    ProductListView,
    OrderSummaryView,
    CheckoutView,
    OrderListView,
)

app_name = 'core'

urlpatterns = [
    path('my-order/', OrderListView.as_view(), name='my-order'),
    path('ProductList/', ProductListView.as_view(), name='product-list'),
    path('product-detail/<pk>/', ProductDetailView.as_view(), name='product'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]