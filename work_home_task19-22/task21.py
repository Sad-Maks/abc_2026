# python
import os
print("cwd:", os.getcwd())
print("exists:", os.path.exists("config_default.txt"))
print("listdir:", os.listdir("."))

# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# Читаем шаблон
with open("config_default.txt", "r", encoding="utf-8") as file:
    template = file.read()

# Разбиваем на строки и обрабатываем каждую
result_lines = []

for line in template.split("\n"):
    # Ищем строки с параметром вида "ключ = ?"
    if "=" in line and "?" in line:
        # Извлекаем имя параметра (до знака "=")
        param = line.split("=")[0].strip()

        # Проверяем, есть ли такое значение в словаре
        if param in config_values:
            value = config_values[param]

            # Форматируем значение в зависимости от типа
            if isinstance(value, str):
                formatted_value = f'"{value}"'
            else:
                formatted_value = str(value)

            # Заменяем "?" на значение, сохраняя выравнивание
            line = line.replace("?", formatted_value)

    result_lines.append(line)

# Записываем результат в config.txt
with open("config.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(result_lines))

print("Файл config.txt успешно создан!")