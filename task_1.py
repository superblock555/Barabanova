import csv

with open('products.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';')
    z = []
    answer = list(reader)[1:]
    for Category, product, Date, Price, Count in answer:
        z.append([Category, product, Date, Price, Count, float(Price)*float(Count)])


with open("products_new.csv", 'w', encoding="utf8", newline='') as file:
    w = csv.writer(file)
    w.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    w.writerows(z)
