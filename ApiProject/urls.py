from django.urls import path
from .views import OrderStatusView, OrderStatusItemView

urlpatterns = [
    path('orderStatus/',OrderStatusView.as_view(), name='customer_order_status'),
    path('orderStatus/<pk>/',OrderStatusItemView.as_view(),name='item_order_status'),
]