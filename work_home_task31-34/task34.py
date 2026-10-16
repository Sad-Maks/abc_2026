class Product:
    """Класс товара с защитой от отрицательной цены."""

    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        self._price = 0 if value < 0 else value

    def __repr__(self):
        """Удобное представление товара для отладки."""
        return f"Product('{self.name}', {self.price})"


class Order:
    """Класс заказа — хранит список товаров (композиция)."""

    def __init__(self):
        # Внутренний список товаров
        self._products = []

    def add_product(self, product):
        """Добавляет товар в заказ."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self._products.append(product)

    def remove_product(self, product):
        """
        Удаляет товар из заказа.
        Если товара нет — ничего не делает.
        """
        if product in self._products:
            self._products.remove(product)
        else:
            print(f"Товар {product} отсутствует в заказе")

    @property
    def total_price(self):
        """
        Вычисляет общую стоимость заказа.
        Суммирует цены всех товаров в списке.
        """
        return sum(product.price for product in self._products)

    @property
    def products(self):
        """Возвращает копию списка товаров (для защиты от прямого изменения)."""
        return self._products.copy()

    def __repr__(self):
        return f"Order({self._products})"


book = Product("Book", 10)
pen = Product("Pen", 2)

order = Order()
order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}")  # 12