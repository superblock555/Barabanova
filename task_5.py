import csv

with open('products.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    data = sorted(reader, key=lambda x: x['Count'])

count = 0
for el in data:
    print(
        f"{el['Category']} {el['Count']}")
    count += 1
    if count == 10:
        break
