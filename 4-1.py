from math import pi

n = input('Введите число точности округления: ')
print(round(pi, len(n) - n.find('.') - 1))
