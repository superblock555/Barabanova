import csv

with open('products.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';')
    z = []
    answer = list(reader)[1:]
    for Category, product, Date, Price, Count in answer:
        promo = Category[:2].upper() + str(Date)[:2] + product[-2:][::-1].upper() + str(Date)[4] + str(Date)[3]
        z.append([Category, product, Date, Price, Count, promo])

with open("product_promo.csv", 'w', encoding="utf8", newline='') as file:
    w = csv.writer(file)
    w.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    w.writerows(z)
