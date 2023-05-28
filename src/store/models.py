from django.db import models


class OrderInfo(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # Складской блок
    warehouse_block = models.CharField(verbose_name="Складской блок", max_length=1)
    # Способ отгрузки
    mode_of_shipment = models.CharField(verbose_name="Способ отгрузки", max_length=20)
    # количество звонков, сделанных с запросом на отгрузку
    customer_care_calls = models.PositiveIntegerField(
        verbose_name="Количество звонков, сделанных с запросом на отгрузку"
    )
    # Рейтинг клиентов
    # Customer_rating = models.PositiveIntegerField(verbose_name="User Rating")
    # Стоимость продукта
    # Cost_of_the_Product = models.ForeignKey(verbose_name="Product cost")
    # Количество предыдущих покупок.
    prior_purchases = models.PositiveIntegerField(
        verbose_name="Количество предыдущих покупок"
    )
    # Важность продукта
    product_importance = models.CharField(
        verbose_name="Важность продукта", max_length=20
    )
    # Пол
    gender = models.CharField(verbose_name="Пол", max_length=1)
    # Скидка
    discount_offered = models.PositiveIntegerField(verbose_name="Скидка")
    # Вес в граммах
    # Weight_in_gms = models.PositiveIntegerField(verbose_name="Weight in grams")
    # Достигнуто вовремя? 0 - вовремя и наоборот
    reached_on_time = models.PositiveIntegerField(
        verbose_name="Достигнуто вовремя? 0 - вовремя и наоборот"
    )

    id_user = models.ForeignKey(
        "users.User",
        verbose_name="user ID",
        on_delete=models.CASCADE,
    )

    id_product = models.ForeignKey(
        "Product", verbose_name="product ID", on_delete=models.CASCADE
    )

    class Meta:
        pass

    def __str__(self):
        return f"ID user:{self.id_user} - {self.id_product.name}"


class Product(models.Model):
    name = models.CharField(unique=False, max_length=100000)
    image = models.ImageField(upload_to="images", height_field=None)
    cost = models.PositiveIntegerField(verbose_name="Цена")
    # Вес в граммах
    weight = models.PositiveIntegerField(verbose_name="Вес в граммах")
    # Рейтинг клиентов
    rating = models.PositiveIntegerField(verbose_name="Рейтинг")

    def __str__(self):
        return f"{self.id} - {self.name}"
