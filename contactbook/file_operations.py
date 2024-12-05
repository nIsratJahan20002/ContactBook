import json

def save_to_file(contacts, filename="contacts.txt"):
    """Saves contacts to a file."""
    with open(filename, "w") as file:
        file.write(json.dumps(contacts))

def load_from_file(filename="contacts.txt"):
    """Loads contacts from a file."""
    try:
        with open(filename, "r") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return []
