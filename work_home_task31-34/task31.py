class Temperature:
    """Класс для работы с температурой. Внутренне хранит значение в Цельсиях."""

    def __init__(self, celsius=0):
        # Внутреннее хранилище — всегда в Цельсиях
        self._celsius = celsius

    @property
    def celsius(self):
        """Возвращает температуру в градусах Цельсия."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Устанавливает температуру в градусах Цельсия."""
        self._celsius = value

    @property
    def fahrenheit(self):
        """Возвращает температуру в градусах Фаренгейта."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Устанавливает температуру в Фаренгейтах, конвертируя в Цельсии."""
        self._celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        """Возвращает температуру в Кельвинах."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        """Устанавливает температуру в Кельвинах, конвертируя в Цельсии."""
        self._celsius = value - 273.15


t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")