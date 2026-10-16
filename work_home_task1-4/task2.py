# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

# Преобразование age (корректно)
age_int = int(age)
print(f"age: {age_int}, тип: {type(age_int)}")

# Преобразование foo (вызовет ошибку, если не обработать)
try:
    foo_int = int(foo)
    print(f"foo: {foo_int}, тип: {type(foo_int)}")
except ValueError:
    print(f"foo: '{foo}' нельзя преобразовать в число, так как там есть буквы.")


# Преобразуйте переменную age в Boolean
age_bool = bool("123abc")
print(f"age_bool: {age_bool}, тип: {type(age_bool)}") 
# Любая непустая строка в Python дает True


# Преобразуйте переменную flag в Boolean
flag = 1
flag_bool = bool(flag)
print(f"flag_bool: {flag_bool}, тип: {type(flag_bool)}")
# 1 преобразуется в True


# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

bool_one = bool(str_one)
bool_two = bool(str_two)
print(f"bool_one: {bool_one}, тип: {type(bool_one)}") # True (непустая строка)
print(f"bool_two: {bool_two}, тип: {type(bool_two)}") # False (пустая строка)


# Преобразуйте значение 0 и 1 в Boolean
print(f"bool(0): {bool(0)}") # False
print(f"bool(1): {bool(1)}") # True


# Преобразуйте False в строку
false_str = str(False)
print(f"false_str: '{false_str}', тип: {type(false_str)}")