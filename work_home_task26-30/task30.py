# 1. Лямбда для максимума из двух чисел
max_of_two = lambda a, b: a if a > b else b
print("Максимум:", max_of_two(10, 25))

# 2. Проверка вхождения в диапазон 1..130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
checks = list(map(lambda x: 1 <= x <= 130, mass))
print("Проверки:", checks)

# 3. Фильтрация нечётных
list_ = [10, 11, 14, 25, 33, 36, 100, 101]
odd_numbers = list(filter(lambda val: val % 2 != 0, list_))
print("Нечётные:", odd_numbers)

# 4. Сортировка по .mp3
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
sorted_files = sorted(files, key=lambda f: not f.endswith('.mp3'))
print("Отсортированные файлы:", sorted_files)