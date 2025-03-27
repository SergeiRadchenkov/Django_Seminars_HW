from django.shortcuts import render
from .models import Client, Product, Order, OrderProduct


def create_client(name, email, phone_number, address):
    """
    Создание нового клиента.
    """
    client = Client.objects.create(
        name=name,
        email=email,
        phone_number=phone_number,
        address=address
    )
    return client


def create_product(name, description, price, quantity):
    """
    Создание нового товара.
    """
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        quantity=quantity
    )
    return product


def create_order(client_id, product_quantities):
    """
    Создание нового заказа.
    """
    client = Client.objects.get(id=client_id)
    order = Order.objects.create(client=client)
    total_amount = 0

    for product_id, quantity in product_quantities.items():
        product = Product.objects.get(id=product_id)
        if product.quantity < quantity:
            raise ValueError(f"Недостаточно товара: {product.name}")
        product.quantity -= quantity
        product.save()

        OrderProduct.objects.create(order=order, product=product, quantity=quantity)
        total_amount += product.price * quantity

    order.total_amount = total_amount
    order.save()

    return order


def get_client_orders(client_id, sort_by="order_date", limit=None):
    """
    Получить все заказы клиента.
    """
    orders = Order.objects.filter(client_id=client_id).order_by(sort_by)
    if limit:
        orders = orders[:limit]
    return orders


def search_products_by_name(product_name, sort_by="name", limit=None):
    """
    Поиск товаров по названию.
    """
    products = Product.objects.filter(name__icontains=product_name).order_by(sort_by)
    if limit:
        products = products[:limit]
    return products


def delete_client(client_id):
    """
    Удалить клиента и все его заказы.
    """
    client = Client.objects.get(id=client_id)
    client.delete()
