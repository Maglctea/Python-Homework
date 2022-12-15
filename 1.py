weekday = int(input('Введите номер дня: '))
if 1 > weekday or weekday > 7:
    print("Такого дня нет")
elif 0 < weekday < 6:
    print("Рабочий")
else:
    print("Выходной")
