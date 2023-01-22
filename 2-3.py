# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:
# - Для n=4 
# {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# сумма 9.06
import msvcrt

n = int(input('Введите число: '))
l = {}
sum = 0

for i in range(1, n + 1):
    l[i] = round((1 + (1 / i)) ** i, 2)
    sum += l[i]

print(l)
msvcrt.getch()
print('Сумма', sum)