def sort_contact(contacts, sort_type):
    serialize_contacts= []
    [serialize_contacts.append(contact.split('|')) for contact in contacts]
    serialize_contacts = sorted(serialize_contacts, key=lambda contact: contact[sort_type-1])

    with open('contacts.txt', 'w', encoding='utf-8') as file:
        for contact in serialize_contacts:
            file.write('|'.join(contact).replace("\n","")+'\n')

