from django.urls import path
from .views import client_orders, client_ordered_products


urlpatterns = [
    path('client/<int:client_id>/orders/', client_orders, name='client_orders'),
    path('client/<int:client_id>/ordered-products/', client_ordered_products, name='client_ordered_products'),
]
