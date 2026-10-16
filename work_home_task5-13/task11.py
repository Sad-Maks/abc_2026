# Получаем номер месяца через input()
month = int(input("Введите номер месяца (1-12): "))

# Определяем время года
if month == 12 or month == 1 or month == 2:
    season = "зима"
elif month == 3 or month == 4 or month == 5:
    season = "весна"
elif month == 6 or month == 7 or month == 8:
    season = "лето"
elif month == 9 or month == 10 or month == 11:
    season = "осень"
else:
    season = None

# Выводим результат
if season is not None:
    print(f"Время года: {season}")
else:
    print("Ошибка: месяц должен быть от 1 до 12!")