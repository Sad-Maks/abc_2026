# Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}

# Даны читатели газет
readers_magazines = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

# Находим пользователей, кто читает и книги, и газеты
# Пересечение множеств
readers_both = readers_books & readers_magazines

# Выводим результат
print(f"Читатели книг: {readers_books}")
print(f"Читатели газет: {readers_magazines}")
print(f"Читают и книги, и газеты: {readers_both}")