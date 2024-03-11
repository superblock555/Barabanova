import csv

with open('products.csv', encoding='utf8') as f:
    reader = list(csv.DictReader(f, delimiter=';', quotechar='"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while float(reader[j]['Price per unit'] if reader[j]['Price per unit'] != 'None' else 0) < float(
                key['Price per unit'] if key['Price per unit'] != 'None' else 0) and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
            reader[j + 1] = key

count = 1
for el in reader:
    print(
        f"В категории: {el['Category']} самый дорогой товар: {el['product']} его цена за единицу товара составляет "
        f"{el['Count']}")
    break
