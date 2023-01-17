# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

def remove(s, del_str):
    list_str = s.split()
    result = ''
    for i in list_str:
        if del_str not in i:
            result += i + ' '
    return result

s = input('Введите строку: ')
print(remove(s, 'абв'))