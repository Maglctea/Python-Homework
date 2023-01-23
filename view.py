def get_action():
    return int(input('1). Добавить контакт.\n2). Получить все контакты.\n3). Сортировать контакты.\n4). Выход.\n>>> '))

def create_contact():
    contact = {}
    contact['id'] = int(input('Введите ID: '))
    contact['name'] = input('Введите Имя: ')
    contact['surname'] = input('Введите Фамилию: ')
    contact['description'] = input('Введите Описание: ')
    return contact

def print_contact(contacts, type_print):
    for contact in contacts:
        contact_info = contact.split('|')
        print('-' * 20)
        if type_print == 1:
            print('ID:', contact_info[0])
        print('Имя:', contact_info[1])
        print('Фамилия:', contact_info[2])        
        if type_print == 1:
            print('Описание:', contact_info[3])
    input('Нажмите Enter для продолжения..\n')

def get_sort_type():
    return int(input('1). Сортировка по ID.\n2). Сортировка по имени.\n>>> '))

def get_print_type():    
    return int(input('1). Полный вывод.\n2). Короткий вывод.\n>>> '))