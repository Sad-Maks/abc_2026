class Product:
    """Класс товара с защитой от отрицательной цены."""

    def __init__(self, name, price=0):
        self.name = name
        self.price = price  # используется сеттер

    # ==================== NAME ====================
    @property
    def name(self):
        """Возвращает название товара."""
        return self._name

    @name.setter
    def name(self, value):
        """Устанавливает название товара (простая строка)."""
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        self._name = value

    # ==================== PRICE ====================
    @property
    def price(self):
        """Возвращает цену товара."""
        return self._price

    @price.setter
    def price(self, value):
        """
        Устанавливает цену товара.
        Если значение отрицательное — устанавливается 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")

        if value < 0:
            self._price = 0
        else:
            self._price = value


# ==================== Пример использования ====================
product = Product("Book", 10)
print(product.price)   # 10

product.price = -5
print(product.price)   # 0