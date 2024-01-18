#CONTACT BOOK

contacts = {}

def add_contact():
    name = input("Enter the name of the person: ")
    phone_number = input("Enter the phone number of the person: ")
    email_id = input("Enter the email-id of the person: ")
    address = input("Enter the address of the person: ")

    contacts[name] = {'phone number': phone_number, 'email-id': email_id, 'address': address}
    print(f"Contact '{name}' added successfully!\n")

def view_contact_list():
    if not contacts:
        print("No contacts found!\n")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone number: {details['phone number']}")
    print()

def search_contact():
    query = input("Enter the name or phone number of the person to search: ")
    found_contacts = []
    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details['phone number']:
            found_contacts.append((name, details))
    if not found_contacts:
        print("No matching contacts found.\n")
        return

    print("\nSearch Result:")
    for name, details in found_contacts:
        print(f"Name: {name}, Phone number: {details['phone number']}")
    print()

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone_number = input("Enter the new phone number: ")
        email_id = input("Enter the new email-id: ")
        address = input("Enter the new address: ")

        contacts[name] = {'phone number': phone_number, 'email': email_id, 'address': address}
        print(f"Contact '{name}' updated successfully.\n")
    else:
        print(f"Contact '{name}' not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print(f"Contact '{name}' not found.\n")

while True:
    print("****** CONTACT BOOK ******")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.\n")
