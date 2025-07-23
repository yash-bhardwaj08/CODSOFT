contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(" Contact added successfully!")

def view_contacts():
    if not contacts:
        print(" No contacts found.")
        return
    print("\n Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']}")

def search_contact():
    key = input("Search by name or phone: ").lower()
    found = False
    for contact in contacts:
        if key in contact['name'].lower() or key in contact['phone']:
            print("\nContact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    key = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == key:
            print("Enter new details (leave blank to keep current):")
            contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    key = input("Enter the name of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == key:
            del contacts[i]
            print("Contact deleted.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
