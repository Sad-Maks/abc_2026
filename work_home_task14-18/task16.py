# База данных пользователей
users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan',  'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

# Выводим меню выбора типа сортировки
print("1. По возрасту")
print("2. По первой букве")
print("3. По группе")

# Получаем тип сортировки
sort_type = input("\nтип сортировки: ").strip()

# Получаем критерий поиска
criterion = input("Ввидите критерии поиска: ").strip()

# Переменная для результата
result = []

# Применяем фильтр в зависимости от выбора
if sort_type == "1":
    # Фильтр по возрасту: возраст больше введённого
    try:
        age_limit = int(criterion)
        result = [user for user in users if user['age'] > age_limit]
    except ValueError:
        print("Ошибка: возраст должен быть числом!")

elif sort_type == "2":
    # Фильтр по первой букве логина (без учёта регистра)
    first_letter = criterion[0].lower()
    result = [user for user in users if user['login'][0].lower() == first_letter]

elif sort_type == "3":
    # Фильтр по группе
    result = [user for user in users if user['group'] == criterion]

else:
    print("Ошибка: неверный тип сортировки!")

# Выводим результат
if result:
    print("\nРезультат:")
    for user in result:
        # Склонение слова "год/года/лет" в зависимости от возраста
        age = user['age']
        if 11 <= age % 100 <= 14:
            age_word = "лет"
        elif age % 10 == 1:
            age_word = "год"
        elif age % 10 in (2, 3, 4):
            age_word = "года"
        else:
            age_word = "лет"

        print(f"Пользователь: '{user['login']}' возраст {age} {age_word} , группа  \"{user['group']}\"")
else:
    print("\nНичего не найдено.")

