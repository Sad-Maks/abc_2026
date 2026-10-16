# Считываем строку
text = input("Введите строку: ")

# Разбиваем строку на слова (по пробелам)
words = text.split()

# Список для результата
result = []

for word in words:
    # Проверяем, является ли слово числом
    if word.isdigit():
        number = int(word)
        # Проверяем, что число в диапазоне 1-26
        if 1 <= number <= 26:
            # Преобразуем число в букву: 1 -> 'a', 2 -> 'b', ...
            # ord('a') = 97, поэтому 97 + number - 1 = 96 + number
            letter = chr(96 + number)
            result.append(letter)
        else:
            # Число вне диапазона — оставляем как есть
            result.append(word)
    else:
        # Не число — оставляем без изменений
        result.append(word)

# Собираем результат обратно в строку через пробел
print(" ".join(result))