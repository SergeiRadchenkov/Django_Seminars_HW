from django.urls import path
from .views import client_orders, client_ordered_products, edit_product, product_list


urlpatterns = [
    path('client/<int:client_id>/orders/', client_orders, name='client_orders'),
    path('client/<int:client_id>/ordered-products/', client_ordered_products, name='client_ordered_products'),
    path('product/<int:pk>/edit/', edit_product, name='edit_product'),
    path('product/', product_list, name='product_list'),
]
