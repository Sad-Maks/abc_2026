# Получаем данные через input()
unit = int(input("Введите номер единицы массы (1-5): "))
M = float(input("Введите массу тела M: "))


if unit == 1:      # килограмм
    kg = M
elif unit == 2:    # миллиграмм
    kg = M / 1_000_000
elif unit == 3:    # грамм
    kg = M / 1_000
elif unit == 4:    # тонна
    kg = M * 1_000
elif unit == 5:    # центнер
    kg = M * 100
else:
    kg = None

# Выводим результат
if kg is not None:
    print(f"Масса в килограммах: {kg} кг")
else:
    print("Ошибка: номер единицы массы должен быть от 1 до 5!")