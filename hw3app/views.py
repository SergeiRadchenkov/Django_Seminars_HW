from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order, OrderProduct
from django.utils import timezone
from datetime import timedelta


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


def client_orders(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    orders = client.orders.all()
    return render(request, 'client_orders.html', {'client': client, 'orders': orders})


def client_ordered_products(request, client_id):
    # Получаем клиента по ID
    client = get_object_or_404(Client, id=client_id)

    # Получаем текущую дату
    today = timezone.now().date()

    # Фильтруем заказы клиента за последние 7, 30 и 365 дней
    one_week_ago = today - timedelta(days=7)
    one_month_ago = today - timedelta(days=30)
    one_year_ago = today - timedelta(days=365)

    # Получаем заказы клиента за последние 7 дней
    orders_last_week = Order.objects.filter(client=client, order_date__gte=one_week_ago)
    # Получаем заказы клиента за последние 30 дней
    orders_last_month = Order.objects.filter(client=client, order_date__gte=one_month_ago)
    # Получаем заказы клиента за последние 365 дней
    orders_last_year = Order.objects.filter(client=client, order_date__gte=one_year_ago)

    # Создаем набор товаров, чтобы избежать повторений
    products_last_week = set()
    products_last_month = set()
    products_last_year = set()

    # Добавляем товары в наборы, чтобы они не повторялись
    for order in orders_last_week:
        for order_product in order.orderproduct_set.all():
            products_last_week.add(order_product.product)

    for order in orders_last_month:
        for order_product in order.orderproduct_set.all():
            products_last_month.add(order_product.product)

    for order in orders_last_year:
        for order_product in order.orderproduct_set.all():
            products_last_year.add(order_product.product)

    # Передаем данные в шаблон
    context = {
        'client': client,
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    }

    return render(request, 'client_ordered_products.html', context)
