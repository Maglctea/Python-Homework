from random import sample

list = sample(range(0, 100), 3)
print(list)

with open('output.txt', 'w') as f:
    for i in list:
        f.write(f'k={i} => 2*x**{i}+4*x+5=0 x**{i}+5=0 10*x**{i}=0\n')
