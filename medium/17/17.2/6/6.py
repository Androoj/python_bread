file = open('prices.txt', encoding='utf-8')

total_amount = 0

for row in file:
    name, quantity, price = row.split('\t')
    total_amount += int(quantity) * int(price)

print(total_amount)

file.close()
