from random import randint

def get_rand_list(count, min=0, max=10):
    array = []
    for i in range(count):
        array.append(randint(min, max))
    return array

len_list = int(input('Введите размер списка: '))

list = get_rand_list(len_list, max=15)
print('Исходный список:', list)

for i in range(len(list) * 2):
    a = randint(0, len(list) - 1)
    b = randint(0, len(list) - 1)
    list[a], list[b] = list[b], list[a]

print('Перемешанный список:',list)