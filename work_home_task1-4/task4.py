x = 20
y = 45
z = 81

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print(f"Наибольшее число {largest}")