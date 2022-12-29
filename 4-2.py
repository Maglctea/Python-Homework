def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

n = int(input('Введите число: '))
print(n,' = ', ' * '.join(map(str, primfacs(n))))
