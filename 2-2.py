def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Введите число: '))
l = []
for i in range(1, n + 1):
    l.append(factorial(i))

print(l)