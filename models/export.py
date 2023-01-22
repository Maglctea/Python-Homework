def export_contact(id, name, surname, description):
    with open('contacts.txt', 'a', encoding='utf-8') as file:
        file.write(f'{id}|{name}|{surname}|{description}\n')