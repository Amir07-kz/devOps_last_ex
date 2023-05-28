def queries_prod(product_id: int) -> str:
    product: str = f"""
    SELECT
        name,
        warehouse_block,
        mode_of_shipment,
        customer_care_calls,
        prior_purchases,
        product_importance,
        gender,
        discount_offered,
        reached_on_time,
        image,
        cost,
        weight,
        rating
    FROM store_orderinfo
    LEFT JOIN store_product sp on store_orderinfo.id_product_id = sp.id
    WHERE store_orderinfo.id = {product_id};
    """
    return product
