n = input('Введите число: ')
result = ''

while n > 0:
    result = result + str(n % 2)
    n = n // 2

print(result[::-1])