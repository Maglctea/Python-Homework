def nfib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return nfib(n + 2) - nfib(n + 1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib_list = []
n = abs(int(input('Введите число: ')))

for i in range(-n, 0):
    fib_list.append(nfib(i))
for i in range(0, n + 1):
    fib_list.append(fib(i))

print(fib_list)