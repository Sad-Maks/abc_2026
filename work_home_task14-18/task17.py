# Заданы множества
# все пользователи
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}

# Вычисляем пользователей online
# Online = все пользователи минус те, кто offline
online_users = all_users - offline_users

# Выводим результат
print(f"Все пользователи: {all_users}")
print(f"Не в сети: {offline_users}")
print(f"Онлайн: {online_users}")

