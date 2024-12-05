from contact_operations import add_contact, delete_contact, search_contact
from file_operations import save_to_file, load_from_file
from validation import validate_name, validate_phone

def main():
    contacts = load_from_file()
    while True:
        print("\n=== Contact Book Management ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = inaput("Enter Name: ")
                validate_name(name)
                phone = input("Enter Phone Number: ")
                validate_phone(phone)
                email = input("Enter Email: ")
                address = input("Enter Address: ")

                new_contact = {"name": name, "phone": phone, "email": email, "address": address}
                add_contact(contacts, new_contact)
                save_to_file(contacts)
                print("Contact added successfully!")

            elif choice == "2":
                print("\n=== All Contacts ===")
                for contact in contacts:
                    print(contact)

            elif choice == "3":
                query = input("Enter search query (name/phone/email): ")
                results = search_contact(contacts, query)
                if results:
                    for result in results:
                        print(result)
                else:
                    print("No contacts found.")

            elif choice == "4":
                identifier = input("Enter Name or Phone to delete: ")
                contacts = delete_contact(contacts, identifier)
                save_to_file(contacts)
                print("Contact deleted successfully!")

            elif choice == "5":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
