import csv

algoritm = ["C4.5", "k - means", "Метод опорных векторов",
 "Apriori", "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"
]

with open("algoritm.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for i, name in enumerate(algoritm, start=1):
        writer.writerow([i, name])

print("Файл algoritm.csv успешно создан!")