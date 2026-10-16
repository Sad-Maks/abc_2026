# Данные две переменные:
age = 36.6
temperature = 25

print(f"До обмена: age = {age}, temperature = {temperature}")

# Обмен значениями местами 
age, temperature = temperature, age

print(f"После обмена: age = {age}, temperature = {temperature}")