import json
import logging
from typing import Any

from django.db import connection
from django.db.models import QuerySet, Count, Sum
from django.db.models.functions import TruncMonth

from store.models import Product, OrderInfo
from store.queries import queries_prod


def execute_product() -> dict:
    """
    Выводит весь имеющийся товар
    """
    products: QuerySet[Product] = Product.objects.all()
    dictionary: list[Any, list[int | str]] = []
    for x in products:
        dictionary.append(
            {
                x.name: {
                    "id": x.id,
                    "image": json.dumps(str(x.image.url)),
                    "cost": x.cost,
                    "weight": x.weight,
                    "rating": x.rating,
                }
            }
        )
    print(json.dumps(dictionary, indent=4))
    return dictionary


def product_character(product_id: int) -> dict:
    """
    Возвращает характеристику конкретного товара по id
    """
    cursor = None
    dictionary: list[Any, list[int | str]] = []
    try:
        cursor = connection.cursor()
        cursor.execute(queries_prod(product_id=product_id))
        res = cursor.fetchall()
        for i, obj in enumerate(res):
            lst = [el for el in obj]
            lst.pop(1)
            # dictionary[obj[0]] = lst
            dictionary.append(
                {
                    obj[0]: {
                        "warehouse_block": obj[1],
                        "mode_of_shipment": obj[2],
                        "customer_care_calls": obj[3],
                        "prior_purchases": obj[4],
                        "product_importance": obj[5],
                        "gender": obj[6],
                        "discount_offered": obj[7],
                        "reached_on_time": obj[8],
                        "image": obj[9],
                        "cost": obj[10],
                        "weight": obj[11],
                        "rating": obj[12],
                    }
                }
            )
            print(json.dumps(dictionary, indent=4))
    except Exception as e:
        logging.warning(f"{e}")
    finally:
        if cursor is not None:
            cursor.close()
    return dictionary


def the_number_of_shipments_from_the_warehouse_in_each_month() -> dict:
    """
    Количество отгрузок в каждом месяце
    """
    data = (
        OrderInfo.objects.annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(count=Count("id"))
        .values("month", "count")
    )
    formatted_data = [
        {"date": month["month"].strftime("%m.%Y"), "count": month["count"]}
        for month in data
    ]
    return formatted_data


def number_of_calls_in_each_month() -> dict:
    """
    Количество звонков в каждом месяце
    """
    data = (
        OrderInfo.objects.annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(count=Sum("customer_care_calls"))
        .values("month", "count")
    )
    formatted_data = [
        {"date": month["month"].strftime("%m.%Y"), "count": month["count"]}
        for month in data
    ]
    return formatted_data


def number_of_goods_not_delivered_on_time_in_each_month() -> dict:
    """
    Количество товаров не доставленных в срок в каждом месяце
    """
    data = (
        OrderInfo.objects.annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(count=Sum("reached_on_time"))
        .values("month", "count")
    )
    formatted_data = [
        {"date": month["month"].strftime("%m.%Y"), "count": month["count"]}
        for month in data
    ]
    return formatted_data
