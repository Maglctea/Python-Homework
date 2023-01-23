def import_contacts():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        return file.readlines()