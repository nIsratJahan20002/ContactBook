def add_contact(contacts, new_contact):
    """Adds a new contact after validation."""
    # Check for duplicate phone numbers
    for contact in contacts:
        if contact["phone"] == new_contact["phone"]:
            raise ValueError("Phone number already exists.")
    contacts.append(new_contact)
    return contacts

def delete_contact(contacts, identifier):
    """Deletes a contact by name or phone."""
    for contact in contacts:
        if contact["name"] == identifier or contact["phone"] == identifier:
            contacts.remove(contact)
            return contacts
    raise ValueError("Contact not found.")

def search_contact(contacts, query):
    """Searches contacts based on the query."""
    results = [contact for contact in contacts if query in contact.values()]
    return results
