import csv

with open('products.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    data = sorted(reader, key=lambda x: x['Price per unit'])
    id_p = input()

while (id_p != 'молоко'):
    for el in data:
        if el['Category'] == id_p:
            print(f"В категории: {el['Category']} товар: {el['product']} был куплен {el['Count']} раз")
            break
        else:
            print("Такой категории не существует в нашей БД")
    id_p = input()
