from decimal import Decimal

l = [1.1, 1.2, 3.1, 5., 10.01]

for i in l:
    if i % 1 > 0:
        min = round(Decimal(i % 1), 2)
        max = round(Decimal(i % 1), 2)
        break

for i in l:
    if i % 1 > 0:
        if min > round(Decimal(i % 1), 2):
            min = round(Decimal(i % 1), 2)
        elif max < round(Decimal(i % 1), 2):
            max = round(Decimal(i % 1), 2)

print(max - min)