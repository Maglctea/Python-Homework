def get_action():
    return int(input('1). Добавить контакт.\n2). Получить все контакты.\n3). Сортировать контакты.\n4). Выход.\n>>> '))

def create_contact():
    contact = {}
    contact['id'] = int(input('Введите ID: '))
    contact['name'] = input('Введите Имя: ')
    contact['surname'] = input('Введите Фамилию: ')
    contact['description'] = input('Введите Описание: ')
    return contact