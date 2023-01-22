import view
from models.export import export_contact

def run():
    while True:
        action = view.get_action()
        if action == 1:
            contact = view.create_contact()
            export_contact(**contact)
        elif action == 1:
            pass
        if action == 3:
            pass
        elif action == 4:
            pass
        else:
            print('Ошибка ввода')