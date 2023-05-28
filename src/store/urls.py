from django.urls import path

from store.views import (
    home,
    product_detail,
    graph_detail_number_of_shipments_from_the_warehouse_in_each_month,
    graph_detail_number_of_calls_in_each_month,
    graph_detail_number_of_goods_not_delivered_on_time_in_each_month,
)

urlpatterns = [
    path("", home, name="home"),
    path("<int:product_id>", product_detail, name="product_detail"),
    path(
        "graph_detail_number_of_shipments_from_the_warehouse_in_each_month",
        graph_detail_number_of_shipments_from_the_warehouse_in_each_month,
        name="graph_detail_number_of_shipments_from_the_warehouse_in_each_month",
    ),
    path(
        "graph_detail_number_of_calls_in_each_month",
        graph_detail_number_of_calls_in_each_month,
        name="graph_detail_number_of_calls_in_each_month",
    ),
    path(
        "graph_detail_number_of_goods_not_delivered_on_time_in_each_month",
        graph_detail_number_of_goods_not_delivered_on_time_in_each_month,
        name="graph_detail_number_of_goods_not_delivered_on_time_in_each_month",
    ),
]
