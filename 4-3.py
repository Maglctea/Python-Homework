from random import randint

l1 = [randint(1, 10) for i in range(20)]
l2 = list(set(l1))

print('Исходный список: ', l1)
print('Итоговый список:', l2)