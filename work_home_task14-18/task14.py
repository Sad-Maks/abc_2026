# Исходный массив
mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

# Словарь для хранения индексов: {значение: [список индексов]}
positions = {}

# Заполняем словарь индексами
for i, value in enumerate(mass):
    if value not in positions:
        positions[value] = []
    positions[value].append(i)

# Переменные для хранения глобального минимума
min_distance = float('inf')   # бесконечность
best_value = None
best_indices = None

# Проходим по всем значениям, у которых больше одного индекса
for value, indices in positions.items():
    if len(indices) > 1:
        # Находим минимальное расстояние между соседними индексами
        for i in range(len(indices) - 1):
            distance = indices[i + 1] - indices[i]
            if distance < min_distance:
                min_distance = distance
                best_value = value
                best_indices = (indices[i], indices[i + 1])

# Выводим результаты по каждому значению
for value, indices in positions.items():
    if len(indices) > 1:
        # Находим минимум для данного значения
        local_min = float('inf')
        local_pair = None
        for i in range(len(indices) - 1):
            distance = indices[i + 1] - indices[i]
            if distance < local_min:
                local_min = distance
                local_pair = (indices[i], indices[i + 1])
        print(f"Для числа {value} минимальное расстояние в массиве по индексам: {local_pair[0]} и {local_pair[1]}")
    else:
        print(f"Для числа {value} нет минимального расстояния, т.к. элемент в массиве один.")

# Выводим глобальный минимум
print()
print(f"Минимальное расстояние в массиве: {min_distance} (между индексами {best_indices[0]} и {best_indices[1]}, число {best_value})")