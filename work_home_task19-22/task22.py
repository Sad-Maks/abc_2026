# Ваше решение.
with open("text.txt", "w+t") as f:
    f.write("Hello\n")
    f.seek(0)          # перемещаем указатель в начало
    print(f.read())    # читаем и выводим

f.close()