class User:
    """Класс пользователя с валидацией email и хранением пароля в виде хеша."""

    def __init__(self, email, password):
        # Используем сеттеры для валидации при создании
        self.email = email
        self.password = password  # сохранится хеш

    # ==================== EMAIL ====================
    @property
    def email(self):
        """Возвращает email пользователя."""
        return self._email

    @email.setter
    def email(self, value):
        """Устанавливает email с простой проверкой на наличие '@'."""
        if not isinstance(value, str):
            raise TypeError("Email должен быть строкой")
        if "@" not in value:
            raise ValueError("Email должен содержать символ '@'")
        self._email = value

    # ==================== PASSWORD ====================
    @property
    def password(self):
        """
        Возвращает хеш пароля.
        Прямой доступ к паролю запрещён — только через check_password().
        """
        return self._password_hash

    @password.setter
    def password(self, value):
        """Устанавливает пароль, сохраняя только его хеш."""
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) == 0:
            raise ValueError("Пароль не может быть пустым")
        self._password_hash = hash(value)

    # ==================== ПРОВЕРКА ПАРОЛЯ ====================
    def check_password(self, password):
        """
        Проверяет, соответствует ли переданный пароль сохранённому хешу.
        Возвращает True или False.
        """
        return hash(password) == self._password_hash


# ==================== Пример использования ====================
user = User("test@example.com", "secret")

print(user.email)                      # test@example.com
print(user.check_password("secret"))   # True
print(user.check_password("wrong"))    # False

# Попытка прочитать пароль напрямую
try:
    print(user.password)
except AttributeError as e:
    print(f"AttributeError: {e}")