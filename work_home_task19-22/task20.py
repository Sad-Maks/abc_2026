# Читаем все строки из файла
with open("inverted_sort.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Дописываем строки в обратном порядке в тот же файл
with open("inverted_sort.txt", "a", encoding="utf-8") as file:
    for line in reversed(lines):
        file.write(line)

print("Готово! Строки добавлены в обратном порядке.")