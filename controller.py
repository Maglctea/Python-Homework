import view
from models.export_contact import export_contact
from models.import_contact import import_contacts
from models.sort_contacts import sort_contact

def run():
    while True:
        action = view.get_action()
        if action == 1:
            contact = view.create_contact()
            export_contact(**contact)
        elif action == 2:
            contacts = import_contacts()
            type_print = view.get_print_type()
            view.print_contact(contacts, type_print)
        elif action == 3:       
            type_sort = view.get_sort_type()     
            contacts = import_contacts()
            sort_contact(contacts, type_sort)

        elif action == 4:
            break
        else:
            print('Ошибка ввода')

