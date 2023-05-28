from django.http import JsonResponse
from django.shortcuts import render
from store.services import (
    execute_product,
    product_character,
    the_number_of_shipments_from_the_warehouse_in_each_month,
    number_of_calls_in_each_month,
    number_of_goods_not_delivered_on_time_in_each_month,
)


def home(request):
    """
    Основная страница с товарами
    """
    dictionary: dict = execute_product()
    return JsonResponse(dictionary, status=200, safe=False)


def product_detail(request, product_id):
    """
    Страница с конкретным товаром
    """
    dictionary: dict = product_character(product_id)
    return JsonResponse(dictionary, status=200, safe=False)


def graph_detail_number_of_shipments_from_the_warehouse_in_each_month(request):
    """
    Количество отгрузок в каждом месяце
    """
    dictionary: dict = the_number_of_shipments_from_the_warehouse_in_each_month()
    return JsonResponse(dictionary, status=200, safe=False)


def graph_detail_number_of_calls_in_each_month(request):
    """
    Количество звонков в каждом месяце
    """
    dictionary: dict = number_of_calls_in_each_month()
    return JsonResponse(dictionary, status=200, safe=False)


def graph_detail_number_of_goods_not_delivered_on_time_in_each_month(request):
    """
    Количество товаров не доставленных в срок в каждом месяце
    """
    dictionary: dict = number_of_goods_not_delivered_on_time_in_each_month()
    return JsonResponse(dictionary, status=200, safe=False)


def cart(request):
    """
    Обрабатывает добавление и удаление элементов из корзины и отображает содержимое корзины.
    """
    return render(request, "shop/cart.html")


def checkout(request):
    """
    Оформление заказа
    """
    return render(request, "shop/checkout.html")
