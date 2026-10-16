# Зашифрованная фраза
encrypted = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

# Функция для расшифровки шифра Цезаря с заданным сдвигом
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Определяем базовый код (для строчных и заглавных букв)
            base = ord('a') if char.islower() else ord('A')
            # Сдвигаем букву назад на shift позиций
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            # Не буквы (пробелы, знаки препинания) оставляем как есть
            result += char
    return result

# Перебираем все 26 возможных сдвигов
for shift in range(26):
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Сдвиг {shift:2d}: {decrypted}")