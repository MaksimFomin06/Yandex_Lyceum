import csv

with open('wares.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    products = list(reader)

discounted_products = [product['Name'] for product in products if int(product['Old price']) > int(product['New price'])]

for product_name in discounted_products:
    print(product_name)